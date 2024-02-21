'''Implementar un script para practicar el cálculo de la matriz de confusión'''
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay,f1_score
from sklearn.metrics import classification_report,precision_score,recall_score,accuracy_score

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
y_real1=['manzana','manzana','naranja','naranja','naranja','manzana','naranja','manzana','naranja','naranja']
y_pred1=['manzana','naranja','naranja','naranja','naranja','naranja','naranja','manzana','naranja','naranja']
#!Lo mas sencillo posible funcion confusion_matrix
c1=confusion_matrix(y_real1,y_pred1)
print(c1)
#?Declarando las etiquetas de filas y columnas.
c=confusion_matrix(y_real1, y_pred1,labels=['manzana','naranja'])
labels=['manzana','naranja']
df=pd.DataFrame(c, index = labels, columns = labels)
print(df)
#Construimos la matriz utilizando métodos gráficos que nos
#proporciona seaborn y el método displaay de sklearn.
#================================================================
#disp = ConfusionMatrixDisplay(confusion_matrix=c,display_labels=['manzana','naranja'])
#disp.plot(cmap='inferno')
#================================================================
#TODO:===FORMA SENCILLA DE REPRESENTAR LA MATTRIZ
sns.heatmap(c, annot=True)
plt.title('Matriz de confusión')
plt.xlabel('Valores Predichos')
plt.ylabel('Valores Reales')
plt.show()
target_names = ['Manzanas', 'Naranjas']
print(classification_report(y_real1, y_pred1, target_names=target_names))
#Cuidado a la elección de los labels en el cálculo de métricas.
#En la única que no influye la elección es en Accuracy
print('Accuracy es:',accuracy_score(y_real1, y_pred1))
print('Precisión es:',precision_score(y_real1, y_pred1,labels=labels,pos_label='naranja'))
print('Sensibilidad es:',recall_score(y_real1, y_pred1,labels=labels,pos_label='naranja'))
print('f1_score es:',f1_score(y_real1, y_pred1,labels=labels,pos_label='naranja'))
