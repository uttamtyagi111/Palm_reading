from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from palmreader.utils.image_utils import preprocess_image, extract_features
from palmreader.utils.report_utils import generate_report
import joblib, os

model = joblib.load('palmreader/models/saved_model.pkl')
label_encoder = joblib.load('palmreader/models/label_encoder.pkl')

def home(request):
    if request.method == 'POST' and request.FILES.get('palm_image'):
        image = request.FILES['palm_image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        filepath = fs.path(filename)

        edges = preprocess_image(filepath)
        features = extract_features(edges)
        prediction = model.predict([features])
        traits = label_encoder.inverse_transform(prediction)[0]

        pdf_filename = f'palmreader/reports/{image.name}_report.pdf'
        generate_report(traits, pdf_filename)

        return render(request, 'palmreader/result.html', {
            'image_url': fs.url(filename),
            'traits': traits,
            'pdf_url': '/' + pdf_filename,
        })

    return render(request, 'palmreader/upload.html')
