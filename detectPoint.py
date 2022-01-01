import cv2
import numpy as np

# 포인트 배열 생성
points = np.zeros((4, 2), np.int)
# 포인트 갯수 카운터
point_Counter = 0
# 폰트 생성
font = cv2.FONT_HERSHEY_SIMPLEX

#마우스 콜백 함수
def mousePoints(e, x, y , flags, params):
    global point_Counter
    #마우스 오른쪽버튼 클릭 시 (클릭해서 땔 때 아님)
    if e == cv2.EVENT_LBUTTONDOWN:
        #포인트 정의
        points[point_Counter] = x, y
        point_Counter = point_Counter + 1
        print(points)


def main():
    global point_Counter
    color_img = cv2.imread("targetImg.jpg", cv2.IMREAD_COLOR)

    while True:
        if point_Counter == 4:
            width, height = 450, 350
            pts1 = np.array([points[0], points[1], points[2], points[3]], dtype= np.float32)
            pts2 = np.array([[0, 0], [width, 0], [0, height], [width, height]],  dtype= np.float32)
            #관점 변환 정의
            m = cv2.getPerspectiveTransform(pts1, pts2)
            # 관점 변환 적용
            imgOutput = cv2.warpPerspective(color_img, m, (width, height))
            cv2.imshow("output image", imgOutput)
            if cv2.waitKey(1) & 0xFF == 32:
                break

        for x in range (0,4):
            cv2.circle(color_img,(points[x][0], points[x][1]),3,(0,255,0),cv2.FILLED)

        cv2.imshow("point image", color_img)
        cv2.setMouseCallback("point image", mousePoints)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()