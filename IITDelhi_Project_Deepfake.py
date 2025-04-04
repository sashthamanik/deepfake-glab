{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "mount_file_id": "1-4uEsmmutXpHTbBDz3aGoLlVXHfjKb9p",
      "authorship_tag": "ABX9TyOAlWmHEVADlEOWtStnZ5ep",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sashthamanik/deepfake-glab/blob/main/IITDelhi_Project_Deepfake.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " Install Required Libraries"
      ],
      "metadata": {
        "id": "TxCkLeVfOV4F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install torch torchvision torchaudio\n",
        "!pip install tensorflow keras opencv-python numpy dlib tqdm ffmpeg albumentations\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4CBkMyqANT4Z",
        "outputId": "8271fd70-56b8-4d42-f917-fb142da7249b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: torch in /usr/local/lib/python3.11/dist-packages (2.6.0+cu124)\n",
            "Requirement already satisfied: torchvision in /usr/local/lib/python3.11/dist-packages (0.21.0+cu124)\n",
            "Requirement already satisfied: torchaudio in /usr/local/lib/python3.11/dist-packages (2.6.0+cu124)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from torch) (3.18.0)\n",
            "Requirement already satisfied: typing-extensions>=4.10.0 in /usr/local/lib/python3.11/dist-packages (from torch) (4.13.0)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (from torch) (3.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from torch) (3.1.6)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.11/dist-packages (from torch) (2025.3.0)\n",
            "Collecting nvidia-cuda-nvrtc-cu12==12.4.127 (from torch)\n",
            "  Downloading nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cuda-runtime-cu12==12.4.127 (from torch)\n",
            "  Downloading nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cuda-cupti-cu12==12.4.127 (from torch)\n",
            "  Downloading nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cudnn-cu12==9.1.0.70 (from torch)\n",
            "  Downloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cublas-cu12==12.4.5.8 (from torch)\n",
            "  Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cufft-cu12==11.2.1.3 (from torch)\n",
            "  Downloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-curand-cu12==10.3.5.147 (from torch)\n",
            "  Downloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cusolver-cu12==11.6.1.9 (from torch)\n",
            "  Downloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cusparse-cu12==12.3.1.170 (from torch)\n",
            "  Downloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Requirement already satisfied: nvidia-cusparselt-cu12==0.6.2 in /usr/local/lib/python3.11/dist-packages (from torch) (0.6.2)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /usr/local/lib/python3.11/dist-packages (from torch) (2.21.5)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch) (12.4.127)\n",
            "Collecting nvidia-nvjitlink-cu12==12.4.127 (from torch)\n",
            "  Downloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: triton==3.2.0 in /usr/local/lib/python3.11/dist-packages (from torch) (3.2.0)\n",
            "Requirement already satisfied: sympy==1.13.1 in /usr/local/lib/python3.11/dist-packages (from torch) (1.13.1)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy==1.13.1->torch) (1.3.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from torchvision) (2.0.2)\n",
            "Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/local/lib/python3.11/dist-packages (from torchvision) (11.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->torch) (3.0.2)\n",
            "Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl (363.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m363.4/363.4 MB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (13.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.8/13.8 MB\u001b[0m \u001b[31m74.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (24.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m24.6/24.6 MB\u001b[0m \u001b[31m16.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (883 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m883.7/883.7 kB\u001b[0m \u001b[31m35.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl (664.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m664.8/664.8 MB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl (211.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m211.5/211.5 MB\u001b[0m \u001b[31m5.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl (56.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m56.3/56.3 MB\u001b[0m \u001b[31m14.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl (127.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m127.9/127.9 MB\u001b[0m \u001b[31m6.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl (207.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.5/207.5 MB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (21.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m21.1/21.1 MB\u001b[0m \u001b[31m72.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: nvidia-nvjitlink-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, nvidia-cusparse-cu12, nvidia-cudnn-cu12, nvidia-cusolver-cu12\n",
            "  Attempting uninstall: nvidia-nvjitlink-cu12\n",
            "    Found existing installation: nvidia-nvjitlink-cu12 12.5.82\n",
            "    Uninstalling nvidia-nvjitlink-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-nvjitlink-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-curand-cu12\n",
            "    Found existing installation: nvidia-curand-cu12 10.3.6.82\n",
            "    Uninstalling nvidia-curand-cu12-10.3.6.82:\n",
            "      Successfully uninstalled nvidia-curand-cu12-10.3.6.82\n",
            "  Attempting uninstall: nvidia-cufft-cu12\n",
            "    Found existing installation: nvidia-cufft-cu12 11.2.3.61\n",
            "    Uninstalling nvidia-cufft-cu12-11.2.3.61:\n",
            "      Successfully uninstalled nvidia-cufft-cu12-11.2.3.61\n",
            "  Attempting uninstall: nvidia-cuda-runtime-cu12\n",
            "    Found existing installation: nvidia-cuda-runtime-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-runtime-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-runtime-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cuda-nvrtc-cu12\n",
            "    Found existing installation: nvidia-cuda-nvrtc-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-nvrtc-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-nvrtc-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cuda-cupti-cu12\n",
            "    Found existing installation: nvidia-cuda-cupti-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-cupti-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-cupti-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cublas-cu12\n",
            "    Found existing installation: nvidia-cublas-cu12 12.5.3.2\n",
            "    Uninstalling nvidia-cublas-cu12-12.5.3.2:\n",
            "      Successfully uninstalled nvidia-cublas-cu12-12.5.3.2\n",
            "  Attempting uninstall: nvidia-cusparse-cu12\n",
            "    Found existing installation: nvidia-cusparse-cu12 12.5.1.3\n",
            "    Uninstalling nvidia-cusparse-cu12-12.5.1.3:\n",
            "      Successfully uninstalled nvidia-cusparse-cu12-12.5.1.3\n",
            "  Attempting uninstall: nvidia-cudnn-cu12\n",
            "    Found existing installation: nvidia-cudnn-cu12 9.3.0.75\n",
            "    Uninstalling nvidia-cudnn-cu12-9.3.0.75:\n",
            "      Successfully uninstalled nvidia-cudnn-cu12-9.3.0.75\n",
            "  Attempting uninstall: nvidia-cusolver-cu12\n",
            "    Found existing installation: nvidia-cusolver-cu12 11.6.3.83\n",
            "    Uninstalling nvidia-cusolver-cu12-11.6.3.83:\n",
            "      Successfully uninstalled nvidia-cusolver-cu12-11.6.3.83\n",
            "Successfully installed nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nvjitlink-cu12-12.4.127\n",
            "Requirement already satisfied: tensorflow in /usr/local/lib/python3.11/dist-packages (2.18.0)\n",
            "Requirement already satisfied: keras in /usr/local/lib/python3.11/dist-packages (3.8.0)\n",
            "Requirement already satisfied: opencv-python in /usr/local/lib/python3.11/dist-packages (4.11.0.86)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (2.0.2)\n",
            "Requirement already satisfied: dlib in /usr/local/lib/python3.11/dist-packages (19.24.6)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (4.67.1)\n",
            "Collecting ffmpeg\n",
            "  Downloading ffmpeg-1.4.tar.gz (5.1 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: albumentations in /usr/local/lib/python3.11/dist-packages (2.0.5)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=24.3.25 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (25.2.10)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (0.6.0)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (18.1.1)\n",
            "Requirement already satisfied: opt-einsum>=2.3.2 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (3.4.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from tensorflow) (24.2)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.3 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (5.29.4)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (2.32.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from tensorflow) (75.2.0)\n",
            "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (1.17.0)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (2.5.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.6 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (4.13.0)\n",
            "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (1.17.2)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (1.71.0)\n",
            "Requirement already satisfied: tensorboard<2.19,>=2.18 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (2.18.0)\n",
            "Requirement already satisfied: h5py>=3.11.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (3.13.0)\n",
            "Requirement already satisfied: ml-dtypes<0.5.0,>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (0.4.1)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow) (0.37.1)\n",
            "Requirement already satisfied: rich in /usr/local/lib/python3.11/dist-packages (from keras) (13.9.4)\n",
            "Requirement already satisfied: namex in /usr/local/lib/python3.11/dist-packages (from keras) (0.0.8)\n",
            "Requirement already satisfied: optree in /usr/local/lib/python3.11/dist-packages (from keras) (0.14.1)\n",
            "Requirement already satisfied: scipy>=1.10.0 in /usr/local/lib/python3.11/dist-packages (from albumentations) (1.14.1)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.11/dist-packages (from albumentations) (6.0.2)\n",
            "Requirement already satisfied: pydantic>=2.9.2 in /usr/local/lib/python3.11/dist-packages (from albumentations) (2.11.0)\n",
            "Requirement already satisfied: albucore==0.0.23 in /usr/local/lib/python3.11/dist-packages (from albumentations) (0.0.23)\n",
            "Requirement already satisfied: opencv-python-headless>=4.9.0.80 in /usr/local/lib/python3.11/dist-packages (from albumentations) (4.11.0.86)\n",
            "Requirement already satisfied: stringzilla>=3.10.4 in /usr/local/lib/python3.11/dist-packages (from albucore==0.0.23->albumentations) (3.12.3)\n",
            "Requirement already satisfied: simsimd>=5.9.2 in /usr/local/lib/python3.11/dist-packages (from albucore==0.0.23->albumentations) (6.2.1)\n",
            "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from astunparse>=1.6.0->tensorflow) (0.45.1)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=2.9.2->albumentations) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=2.9.2->albumentations) (2.33.0)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=2.9.2->albumentations) (0.4.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.21.0->tensorflow) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.21.0->tensorflow) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.21.0->tensorflow) (2025.1.31)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.11/dist-packages (from tensorboard<2.19,>=2.18->tensorflow) (3.7)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from tensorboard<2.19,>=2.18->tensorflow) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from tensorboard<2.19,>=2.18->tensorflow) (3.1.3)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich->keras) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich->keras) (2.18.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich->keras) (0.1.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from werkzeug>=1.0.1->tensorboard<2.19,>=2.18->tensorflow) (3.0.2)\n",
            "Building wheels for collected packages: ffmpeg\n",
            "  Building wheel for ffmpeg (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ffmpeg: filename=ffmpeg-1.4-py3-none-any.whl size=6083 sha256=cc70e324c704154d289abdfa84faa97220c22e1066372355bd8aa2220626331c\n",
            "  Stored in directory: /root/.cache/pip/wheels/56/30/c5/576bdd729f3bc062d62a551be7fefd6ed2f761901568171e4e\n",
            "Successfully built ffmpeg\n",
            "Installing collected packages: ffmpeg\n",
            "Successfully installed ffmpeg-1.4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " Extract Frames from Videos"
      ],
      "metadata": {
        "id": "6R1RFqVjORJz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import cv2\n",
        "import os\n",
        "#John.mp4\n",
        "input_dir = \"/content/drive/MyDrive/deepfake/input/\"\n",
        "output_dir = \"/content/drive/MyDrive/deepfake/input/dataset/frames/\"\n",
        "os.makedirs(output_dir, exist_ok=True)\n",
        "\n",
        "for video_name in os.listdir(input_dir):\n",
        "    video_path = os.path.join(input_dir, video_name)\n",
        "    cap = cv2.VideoCapture(video_path)\n",
        "    count = 0\n",
        "\n",
        "    while cap.isOpened():\n",
        "        ret, frame = cap.read()\n",
        "        if not ret:\n",
        "            break\n",
        "        frame_path = os.path.join(output_dir, f\"{video_name}_frame_{count}.jpg\")\n",
        "        cv2.imwrite(frame_path, frame)\n",
        "        count += 1\n",
        "\n",
        "    cap.release()\n"
      ],
      "metadata": {
        "id": "gy4nC94jN2fp"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Label Data (Real vs Fake)"
      ],
      "metadata": {
        "id": "LaCKLraMObQN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import shutil\n",
        "import os\n",
        "\n",
        "real_dir = \"/content/drive/MyDrive/deepfake/input/dataset/real/\"\n",
        "fake_dir = \"/content/drive/MyDrive/deepfake/input/dataset/fake/\"\n",
        "os.makedirs(real_dir, exist_ok=True)\n",
        "os.makedirs(fake_dir, exist_ok=True)\n",
        "\n",
        "for img in os.listdir(\"/content/drive/MyDrive/deepfake/input/dataset/frames/\"):\n",
        "    if \"fake\" in img:\n",
        "        shutil.move(f\"/content/drive/MyDrive/deepfake/input/dataset/frames/{img}\", fake_dir)\n",
        "    else:\n",
        "        shutil.move(f\"/content/drive/MyDrive/deepfake/input/dataset/frames/{img}\", real_dir)"
      ],
      "metadata": {
        "id": "tc2Ij-mQOYdV"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Train the Deepfake Detection Model. We will use EfficientNet - CNN for classification. Load Data Using PyTorch"
      ],
      "metadata": {
        "id": "fLsTFpOHnYbq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import cv2\n",
        "import os\n",
        "import shutil\n",
        "from torchvision import transforms, datasets\n",
        "from torch.utils.data import DataLoader, Subset\n",
        "import torch\n",
        "import numpy as np\n",
        "\n",
        "# --- Extract Frames from Videos ---\n",
        "input_dir = \"/content/drive/MyDrive/deepfake/input/\"\n",
        "output_dir = \"/content/drive/MyDrive/deepfake/input/dataset/frames/\"\n",
        "os.makedirs(output_dir, exist_ok=True)\n",
        "\n",
        "for video_name in os.listdir(input_dir):\n",
        "    video_path = os.path.join(input_dir, video_name)\n",
        "    cap = cv2.VideoCapture(video_path)\n",
        "    count = 0\n",
        "\n",
        "    while cap.isOpened():\n",
        "        ret, frame = cap.read()\n",
        "        if not ret:\n",
        "            break\n",
        "        frame_path = os.path.join(output_dir, f\"{video_name}_frame_{count}.jpg\")\n",
        "        cv2.imwrite(frame_path, frame)\n",
        "        count += 1\n",
        "\n",
        "    cap.release()\n",
        "\n",
        "# --- Label Data (Real vs Fake) ---\n",
        "# Instead of moving the images, we'll create a list of image paths and their labels\n",
        "all_images = []\n",
        "all_labels = []\n",
        "\n",
        "for img in os.listdir(output_dir):\n",
        "    image_path = os.path.join(output_dir, img)\n",
        "    if \"fake\" in img:\n",
        "        all_labels.append(1)  # 1 for fake\n",
        "    else:\n",
        "        all_labels.append(0)  # 0 for real\n",
        "    all_images.append(image_path)\n",
        "\n",
        "# --- Train the Deepfake Detection Model ---\n",
        "transform = transforms.Compose([\n",
        "    transforms.Resize((224, 224)),\n",
        "    transforms.ToTensor(),\n",
        "    transforms.Normalize([0.5], [0.5])\n",
        "])\n",
        "\n",
        "# Create a custom dataset class\n",
        "class DeepfakeDataset(torch.utils.data.Dataset):\n",
        "    def __init__(self, image_paths, labels, transform=None):\n",
        "        self.image_paths = image_paths\n",
        "        self.labels = labels\n",
        "        self.transform = transform\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.image_paths)\n",
        "\n",
        "    def __getitem__(self, idx):\n",
        "        image_path = self.image_paths[idx]\n",
        "        image = cv2.imread(image_path)\n",
        "        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to RGB\n",
        "\n",
        "        if self.transform:\n",
        "            image = self.transform(image)\n",
        "\n",
        "        label = self.labels[idx]\n",
        "        return image, label\n",
        "\n",
        "\n",
        "# Create the dataset\n",
        "dataset = DeepfakeDataset(all_images, all_labels, transform=transform)\n",
        "\n",
        "# Split into train and validation sets (optional but recommended)\n",
        "train_size = int(0.8 * len(dataset))\n",
        "val_size = len(dataset) - train_size\n",
        "train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])\n",
        "\n",
        "# Create data loaders\n",
        "train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)\n",
        "#val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False) # Use if you split into validation set"
      ],
      "metadata": {
        "id": "hnuPPJB5ng86"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Define the Model (EfficientNet)"
      ],
      "metadata": {
        "id": "r7rE8rbTpa8d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch.nn as nn\n",
        "import torchvision.models as models\n",
        "\n",
        "class DeepfakeDetector(nn.Module):\n",
        "    def __init__(self):\n",
        "        super(DeepfakeDetector, self).__init__()\n",
        "        self.model = models.efficientnet_b0(pretrained=True)\n",
        "        self.model.classifier = nn.Sequential(\n",
        "            nn.Linear(1280, 512),\n",
        "            nn.ReLU(),\n",
        "            nn.Linear(512, 1),\n",
        "            nn.Sigmoid()\n",
        "        )\n",
        "\n",
        "    def forward(self, x):\n",
        "        return self.model(x)\n",
        "\n",
        "model = DeepfakeDetector()\n"
      ],
      "metadata": {
        "id": "FxpEUDCkpaot"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Train the Model"
      ],
      "metadata": {
        "id": "EOrP7AbhpgYM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "from torchvision import transforms, datasets\n",
        "from torch.utils.data import DataLoader\n",
        "\n",
        "# Define transformations\n",
        "transform = transforms.Compose([\n",
        "    transforms.ToPILImage(),  # Convert NumPy array to PIL Image if needed\n",
        "    transforms.Resize((224, 224)),\n",
        "    transforms.ToTensor(),  # Convert PIL Image to PyTorch tensor\n",
        "    transforms.Normalize([0.5], [0.5])\n",
        "])\n",
        "\n",
        "# Load dataset correctly\n",
        "class CustomDataset(torch.utils.data.Dataset):\n",
        "    def __init__(self, image_paths, labels, transform=None):\n",
        "        self.image_paths = image_paths\n",
        "        self.labels = labels\n",
        "        self.transform = transform\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.image_paths)\n",
        "\n",
        "    def __getitem__(self, idx):\n",
        "        img = cv2.imread(self.image_paths[idx])  # Read image as NumPy array\n",
        "        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB\n",
        "        label = self.labels[idx]\n",
        "\n",
        "        if self.transform:\n",
        "            img = self.transform(img)  # Apply transformations\n",
        "\n",
        "        return img, torch.tensor(label, dtype=torch.float32)  # Ensure label is tensor\n",
        "\n",
        "# Example dataset setup\n",
        "image_paths = [\"/content/drive/MyDrive/deepfake/input/dataset/real/\", \"/content/drive/MyDrive/deepfake/input/dataset/fake/\"]  # Replace with actual paths\n",
        "labels = [0, 1]  # 0 for real, 1 for fake\n",
        "\n",
        "dataset = CustomDataset(image_paths, labels, transform=transform)\n",
        "train_loader = DataLoader(dataset, batch_size=32, shuffle=True)\n"
      ],
      "metadata": {
        "id": "_uhhH73wpiX8"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Save the Model"
      ],
      "metadata": {
        "id": "Sr8BfG-rqGe8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "torch.save(model.state_dict(), \"/content/drive/MyDrive/deepfake/deepfake_detector.pth\")"
      ],
      "metadata": {
        "id": "vLrYgd7qqGyt"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Test Deepfake Detection"
      ],
      "metadata": {
        "id": "6TciEdjvqTYE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from PIL import Image\n",
        "import torch\n",
        "from torchvision import transforms\n",
        "\n",
        "# Define transformation (Make sure to exclude ToPILImage here)\n",
        "transform = transforms.Compose([\n",
        "    transforms.Resize((224, 224)),\n",
        "    transforms.ToTensor(),  # Converts PIL image directly to tensor\n",
        "    transforms.Normalize([0.5], [0.5])\n",
        "])\n",
        "\n",
        "def detect_deepfake(image_path):\n",
        "    image = Image.open(image_path).convert(\"RGB\")  # Ensure 3-channel RGB\n",
        "    image = transform(image).unsqueeze(0)  # Apply transformations and add batch dimension\n",
        "\n",
        "    model.eval()\n",
        "    with torch.no_grad():\n",
        "        output = model(image)\n",
        "        return \"fake\" if output.item() > 0.5 else \"real\"\n",
        "\n",
        "# Test the function with an image path\n",
        "print(detect_deepfake(\"/content/drive/MyDrive/deepfake/input/dataset/frames/John.mp4_frame_0.jpg\"))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fRtPGcfcqT5N",
        "outputId": "3a5d3f01-668c-4f24-b389-a8c64a2ac2b1"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fake\n"
          ]
        }
      ]
    }
  ]
}
