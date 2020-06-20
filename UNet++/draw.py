import matplotlib.pyplot as plt
import numpy as np

COLORS = np.array(['#FF3333',  # red
                '#0198E1',  # blue
                '#BF5FFF',  # purple
                '#FCD116',  # yellow
                '#FF7216',  # orange
                '#4D9000',  # green
                '#87421F',  # brown
                '#015090',
                'turquoise',
                '#01DE69',
                # '#010069',
                '#00FFFF',
                '#000000'   # black
                ])

if __name__ == "__main__":
    # this file was run after running training routine.
    # it was used to draw acc-epoch curve.
    y = [0.8358187815140893, 0.8317031413315611, 0.8326619987608623, 0.8550549812158306, 
    0.847390177041181, 0.8512589238574306, 0.8564507881805955, 0.8650621733250691, 
    0.8433478939751725, 0.8566875288084255, 0.8589662400732585, 0.8673978881237658, 
    0.8689390348485838, 0.8675744179919653, 0.8534143286695506, 0.8644068399708016, 
    0.8576361235449894, 0.8671441690449739, 0.8685414948018834, 0.8637915761791615, 
    0.8675845270172199, 0.8619858702924161, 0.8602659430218902, 0.8600495257563255, 
    0.8550262659938979, 0.8601945094977944, 0.866207988771643, 0.8680391798915306, 
    0.8744511062765529, 0.8749175515594577, 0.8700531771053904, 0.8289972047002738, 
    0.8646898500878815, 0.8500702886341732, 0.8592688376958006, 0.8724176781871613, 
    0.8549212616364874, 0.8729978068043176, 0.8679823614027361, 0.8618873064917009]

    # this file represents the accuracy output of deep-supervised model.
    y_deep = [0.7924681897173912, 0.8327759705936466, 0.8424255507886351, 0.8360675945355296, 
    0.8373939246307812, 0.8295177086013766, 0.8286272269734615, 0.8168208231754097, 
    0.8390606472811979, 0.8483282756605012, 0.836433357882543, 0.8454199080730868, 
    0.8535026649464362, 0.843209159798184, 0.8306484293298718, 0.8446015187605551, 
    0.8508132475170546, 0.8426749298472859, 0.8407658761252764, 0.84390445009552, 
    0.8457930735130295, 0.841282114555591, 0.8485918386433337, 0.8551360094542809, 
    0.8546002788596068, 0.8447216418650249, 0.8547822706460605, 0.8320765523579154, 
    0.8544748338761398, 0.8564007170045252, 0.8602855148076282, 0.8379801158392003, 
    0.8507282134586353, 0.8591351754171074, 0.8234438514459856, 0.8536506097278984, 
    0.8537624551629291, 0.855250841423863, 0.8423995891263886, 0.8549170374251919]

    # draw the results with uniform format
    x = np.linspace(1, 40, 40)
    plt.title("Relationship between accuracy and epoch")
    plt.xlabel("epoch")
    plt.ylabel("accuracy on test data")
    plt.plot(x, y, color=COLORS[0])
    plt.plot(x, y_deep, color=COLORS[1])
    plt.legend(["Normal", "Deep-supervised"])
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(2))
    plt.show()