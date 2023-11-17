import pygame
import numpy as np


def play():
    pygame.mixer.init()
    pygame.mixer.music.load("./data/beep.mp3")
    pygame.mixer.music.play()


# import numpy as np                    		# 수학 계산 관련 라이브러리
# import matplotlib.pyplot as plt    		# 그래프 (및 그림) 표시를 위한 library
# import torch                          		# 파이토치 관련 라이브러리
# import torch.nn as nn                 		# neural network 관련 라이브러리
#
# import torchvision.datasets as dset   		# 다양한 데이터셋 (MNIST, COCO, ...) 관련 라이브러리
# import torchvision.transforms as transforms   	# 입력/출력 데이터 형태, 크기 등을 조정
# from torch.utils.data import DataLoader        	# 데이터를 적절한 배치 사이즈로 load 할 수 있도록 함.
#
# X = torch.Tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
# Y = torch.Tensor([[0], [0], [0], [1]])
#
# # bs = 4                			# batch_size 는 대개 2^n 형태의 값으로 설정함.
# learning_rate = 0.05      			# 최적 학습률은 최적화 알고리즘 및 batch_size 에 따라 달라짐.
# num_epochs = 2000			# 학습 반복 횟수
#
# class My_Model(nn.Module):
#     def __init__(self):
#         super().__init__()  # parent class 인 nn.Module의 생성자/초기화 함수를 상속함.
#         self.layer = nn.Sequential(
#             nn.Linear(2, 10),    # (1)
#             # nn.ReLU(),
#             nn.Sigmoid(),          # (2)
#             nn.Linear(10, 1),    # (3)
#             nn.Sigmoid(),       # (4)
#         )
#
#     def forward(self, x):  # x.shape = (bs, 1, 28, 28)
#         out_data = self.layer(x)  # out_data.shape = (bs, 10)
#         return out_data
#
#
# model = My_Model()
# loss_func = nn.BCELoss()  # nn.CrossEntropyLoss() = [Softmax + CEL]
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  # Stochastic Gradient Descent
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # cuda는 GPU를 의미함.
# model = model.to(device)  # GPU 사용이 가능한 경우, GPU에서 시뮬레이션 실시
#
#
# for epoch in range(num_epochs+1):
#     prediction = model(X)		# 순전파 과정
#     loss = loss_func(prediction, Y)	# 손실 함수 계산
#
#     optimizer.zero_grad()		# 기울기값 초기화
#     loss.backward()		# 기울기값 계산
#     optimizer.step()		# 가중치 업데이트
#
#     if epoch % 100 == 0:		# 특정 조건 만족할 때마다 현재 진행 상태 표시
#         print(f'Epoch: {epoch:4d}  loss = {loss.item():8.5f}')
#         print('prediction =', prediction.detach().squeeze().numpy())
#         print()
#
# prediction = model(X)				# 실수/확률 형태의 예측 출력값
# pred_final = (prediction > 0.5).float()		# (0 또는 1) 형태의 예측 출력값
# accuracy = (pred_final == Y).float().mean()		# 예측 출력값과 정답값 비교
# print('prediction =', prediction.detach().squeeze().numpy())
# print('pred_final =', pred_final.detach().squeeze().numpy())
# print('target     =', Y.squeeze().numpy())		# 정답값
# print('accuracy   =', accuracy.item()*100, '%')
