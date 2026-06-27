def grade_from_score(score):
    """แปลงคะแนนเป็นเกรดตัวอักษรตามเงื่อนไขในภาพ"""
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'


def main():
    try:
        score = float(input('Enter score: '))
    except ValueError:
        print('กรุณาป้อนตัวเลขคะแนนที่ถูกต้อง')
        return

    grade = grade_from_score(score)
    print(f'Score: {score} -> Grade: {grade}')


if __name__ == '__main__':
    main()
