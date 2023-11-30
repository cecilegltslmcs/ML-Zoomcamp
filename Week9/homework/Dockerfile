FROM agrigorev/zoomcamp-bees-wasps:v2

<<<<<<< HEAD
RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

COPY homework.py .
ENV MODEL_NAME=bees-wasps-v2.tflite

CMD ["homework.lambda_handler"]
=======
COPY requirements.txt .
COPY homework.py .

RUN pip install -r requirements.txt
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

CMD ["homework.lambda_handler"]
>>>>>>> 918ca45 (homework week9)
