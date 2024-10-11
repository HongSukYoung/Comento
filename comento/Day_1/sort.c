#include <stdio.h>

//void sort(int len, int list){
//    int min = 0;
//    for(int i = 0; i<len; i++){
//        for(int j=0; j<i; j++){
//            if(list[i]>list[j]){
//               min = list[j]
//                list[j] = list[i]
//                list[i] = min
//            }
//        }
//    }
//}

void sort(int len, int list[]){
    int min;
    for(int i = 0; i < len - 1; i++){
        for(int j = i + 1; j < len; j++){
            if(list[i] > list[j]){
                min = list[j];
                list[j] = list[i];
                list[i] = min;
            }
        }
    }
}

#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // 임시 배열 생성
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));

    // 데이터를 임시 배열에 복사
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // 병합
    i = 0;  // L 배열의 첫 인덱스
    j = 0;  // R 배열의 첫 인덱스
    k = left;  // 병합될 배열의 첫 인덱스
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // 남은 요소 복사
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // 임시 배열 해제
    free(L);
    free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // 왼쪽과 오른쪽을 나눠서 재귀적으로 정렬
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // 나눠진 배열을 병합
        merge(arr, left, mid, right);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
