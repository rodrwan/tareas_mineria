from sklearn import metrics
from tabulate import tabulate

# file_prefix = './resultados_ind/result_m0'
file_prefix = './resultados_ind/result_m'
ids = [x for x in range(0, 10)]
list_of_files = [file_prefix+str(x) for x in ids]

vectors = None
with open('test_data') as all_vectors:
  all_vectors = all_vectors.read()
  svectors = all_vectors.split("\n")
  if svectors[-1] == "":
      svectors.pop(-1)
  classes = []
  for svect in svectors:
    classes.append(float(svect.split()[0]))

for _file in list_of_files:
  with open(_file, 'r') as rfile:
    result = rfile.read().split("\n")
    if result[-1] == "":
      result.pop(-1)

    final_result = []
    for idx in range(0, len(result)):
      res = float(result[idx])
      if (res < 0):
        final_result.append(-1)
      else:
        final_result.append(1)

    y_test = classes
    y_predicted = final_result
    print "##########################################################################"
    print "##########################################################################"
    print
    print metrics.classification_report(y_test, y_predicted)
    print
    print "Confusion matrix"
    conf_mat = metrics.confusion_matrix(y_test, y_predicted)

    table = [
      ["Entity pred", conf_mat[1][1], conf_mat[1][0]],
      ["Token pred", conf_mat[0][1], conf_mat[0][0]]
    ]
    print tabulate(table, headers=["","Entity real", "Token real"], tablefmt="grid")
    print
    print

    import pylab as pl
    from sklearn.metrics import roc_curve, auc
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y_test, y_predicted)
    roc_auc = auc(fpr, tpr)
    print "Area under the ROC curve : %f" % roc_auc
    # Plot ROC curve
    pl.clf()
    pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    pl.plot([0, 1], [0, 1], 'k--')
    pl.xlim([0.0, 1.0])
    pl.ylim([0.0, 1.0])
    pl.xlabel('False Positive Rate')
    pl.ylabel('True Positive Rate')
    pl.title('ROC para primer grupo de features')
    pl.legend(loc="lower right")
    pl.show()