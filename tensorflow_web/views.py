from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.core.files.temp import NamedTemporaryFile

from .forms import UploadFileForm
from PIL import Image
from weasyprint import HTML

import io
import numpy as np
import tensorflow as tf
import os
import base64

TF_GRAPH = "{base_path}/graph/output_graph.pb".format(
    base_path=os.path.abspath(os.path.dirname(__file__)))
TF_LABELS = "{base_path}/graph/output_labels.txt".format(
    base_path=os.path.abspath(os.path.dirname(__file__)))


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)

    return graph


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader")
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader"))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
    else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(
        dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)

    return result


def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label


def upload_file(request):
    image_temp = NamedTemporaryFile()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file'].read()
            image_data = Image.open(io.BytesIO(data))
            image_data.save(image_temp, image_data.format)
            dict_result = start_label(image_temp.name)
        temp_img_encode = generate_image_uri(image_temp.name)
        pdf_file = generate_pdf_uri(dict_result, temp_img_encode)
        return render(request, 'results.html', {'pdf_file': pdf_file,
                                                'prediction_results': dict_result,
                                                'image_data_uri': temp_img_encode,
                                                'first_prediction_key': next(iter(dict_result)),
                                                'first_prediction_value': next(iter(dict_result.values())),
                                                'exclude_key': [next(iter(dict_result))]})
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def generate_image_uri(image):
    with open(image, "rb") as temp_img:
        temp_img_string = base64.b64encode(temp_img.read())
        temp_img_encode = "data:image/jpeg;base64," + \
                          str(temp_img_string)[2:-1]

    return temp_img_encode


def generate_pdf_uri(dict_data, image):
    dict_result = dict_data
    temp_img_encode = image
    html_string = render_to_string('pdf.html', {'prediction_results': dict_result,
                                                'image_data_uri': temp_img_encode,
                                                'first_prediction_key': next(iter(dict_result)),
                                                'first_prediction_value': next(iter(dict_result.values())),
                                                'exclude_key': [next(iter(dict_result))]})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/temp_file.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('temp_file.pdf') as pdf:
        encoded_pdf = base64.b64encode(pdf.read())
        encoded_pdf_uri = "data:application/pdf;base64," + \
                          str(encoded_pdf)[2:-1]

    return encoded_pdf_uri


def start_label(image):
    file_name = image
    model_file = TF_GRAPH
    label_file = TF_LABELS
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "Placeholder"
    output_layer = "final_result"

    graph = load_graph(model_file)
    t = read_tensor_from_image_file(
        file_name,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
        })
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)

    dict_result = dict()

    for i in top_k:
        dict_result[labels[i]] = str(np.round(results[i] * 100, 4)) + '%'

    return dict_result
