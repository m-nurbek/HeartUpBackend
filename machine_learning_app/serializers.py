from rest_framework import serializers

from . import models


class HeartBeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeartBeatModel
        fields = ('id', 'heart_beat_audio', 'heart_beat_audio_upload_on')

    def validate(self, data):
        value = data['heart_beat_audio']
        if not value.name.lower().endswith('.wav') and not value.name.lower().endswith('.mp3'):
            raise serializers.ValidationError("Invalid file type. Only '.wav' or '.mp3' files are allowed.")
        return value


class ECGSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ECGModel
        exclude = ('patient',)


class UCLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UCLModel
        exclude = ('patient',)


class EchoNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EchoNetModel
        exclude = ('patient',)


class MLDiagnosisSerializer(serializers.ModelSerializer):
    ecg_prediction = serializers.CharField(read_only=True)
    heart_beat_prediction = serializers.CharField(read_only=True)
    ucl_prediction = serializers.CharField(read_only=True)
    echo_net_prediction = serializers.CharField(read_only=True)

    heart_beat = HeartBeatSerializer()
    ecg = ECGSerializer()
    ucl = UCLSerializer()
    echo_net = EchoNetSerializer()

    class Meta:
        model = models.MLDiagnosisModel
        fields = ('id', 'patient', 'heart_beat', 'ecg', 'ucl', 'echo_net',
                  'heart_beat_prediction', 'ecg_prediction', 'ucl_prediction', 'echo_net_prediction',
                  'heart_beat_prediction_on', 'ecg_prediction_on', 'ucl_prediction_on', 'echo_net_prediction_on')
