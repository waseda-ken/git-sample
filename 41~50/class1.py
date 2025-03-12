class SchoolReport:
    def __init__(self,student_name,math_score,jp_score,en_score):
        self.student_name=student_name
        self.math_score=math_score
        self.jp_score=jp_score
        self.en_score=en_score

    def calc_avg_score(self):
        self.sum_score=(self.math_score+self.jp_score+self.en_score)
        avg_score=self.sum_score/3
        return avg_score

sr_a=SchoolReport('田中 A',100,30,50)
avg_a=sr_a.calc_avg_score()
print(f'Aさんの3教科の平均点: {avg_a}')
print(sr_a.sum_score)

sr_b=SchoolReport('鈴木 B',80,70,80)
avg_b=sr_b.calc_avg_score()
print(f'Bさんの3教科の平均点: {avg_b}')

sr_c=SchoolReport('佐藤 C',100,85,90)
avg_c=sr_c.calc_avg_score()
print(f'Cさんの3教科の平均点: {avg_c}')
