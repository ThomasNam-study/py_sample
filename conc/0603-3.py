import os
import time
import sys
import csv
from concurrent import futures

NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()

# 초기 CSV 위치
TARGET_CSV = 'nations.csv'
DEST_DIR = "./csvs/"

HEADER = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority', 'Order Date', 'Order ID', 'Ship Date',
          'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']


def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data


def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)


# 중간 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()


def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return nt


def main(separate_many):
    start_tm = time.time()

    worker = min(20, len(NATION_LS))

    futures_list = []

    # result_cnt = separate_many(NATION_LS)
    # with futures.ThreadPoolExecutor(worker) as executor:
    with futures.ProcessPoolExecutor() as executor:
        # result_cnt = executor.map(separate_many, sorted(NATION_LS))
        for nt in sorted(NATION_LS):
            future = executor.submit(separate_many, nt)
            futures_list.append(future)

            #print('Scheduled for {} : {}'.format(nt, future))
            #print()

    for f in futures.as_completed(futures_list):
        result = f.result()
        done = f.done()
        cancelled = f.cancelled()

        print('Future Result : {}, Done : {}'.format(result, done))

    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'
    # 최종 결과 출력
    # print(msg.format(result_cnt, end_tm))


if __name__ == '__main__':
    main(separate_many)
