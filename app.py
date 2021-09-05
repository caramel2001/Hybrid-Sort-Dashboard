# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
from streamlit import caching
import pandas as pd
import random


def generaterandom(n):

    result = []
    for j in range(1000):
        randomlist = []
        for i in range(0, n):
            N = random.randint(1, 10000)
            randomlist.append(N)
        result.append((randomlist))
    return result


def generaterandom_2(n):

    result = []
    for j in range(100):
        randomlist = []
        for i in range(0, n):
            N = random.randint(1, 1000)
            randomlist.append(N)
        result.append((randomlist))
    return result


def merge_sort(array, left_index, right_index, comp=0):
    global compares
    # recursion ending statement
    if left_index >= right_index:
        return

    # finding middle
    middle = (left_index + right_index)//2

    # recursive call 1
    merge_sort(array, left_index, middle)
    # recurive call 2
    merge_sort(array, middle + 1, right_index)

    # merging the returned arrays after recurrsion
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):

    global compares
    # making copies of list
    left_list = array[left_index:middle+1]
    right_list = array[middle+1:right_index+1]

    # intialising indexes
    left_list_index = 0
    right_list_index = 0
    sorted_index = left_index

    while(left_list_index < len(left_list) and right_list_index < len(right_list)):

        # If left_list has the smaller element, put it in the sorted
        # part and then move forward in left_copy
        if left_list[left_list_index] <= right_list[right_list_index]:
            array[sorted_index] = left_list[left_list_index]
            left_list_index = left_list_index + 1
            # comparison=comparison+1
            #compares = compares+1
        # else put the right_list ement in sorted array
        else:
            array[sorted_index] = right_list[right_list_index]
            right_list_index = right_list_index + 1
            #compares = compares+1

        # increasing sorted index
        sorted_index = sorted_index+1
        compares = compares+1
    # Wran out of elemnt in either one of the list
    # so we will put the remaining elements and add them to the sorted list
    while left_list_index < len(left_list):
        array[sorted_index] = left_list[left_list_index]
        left_list_index = left_list_index + 1
        sorted_index = sorted_index + 1

    while right_list_index < len(right_list):
        array[sorted_index] = right_list[right_list_index]
        right_list_index = right_list_index + 1
        sorted_index = sorted_index + 1


def hybridinsertion_sort(array, start, end):
    global compares
    for index in range(start, end+1):
        for j in range(index, start ,-1):
            if(array[j]<array[j-1]):
                temp = array[j]
                array[j]=array[j-1]
                array[j-1]=temp
                compares = compares+1
            else :
                compares = compares+1
                break


def hybrid_sort(array, left_index, right_index, s):
    global compares
    # finding middle
    middle = (left_index + right_index)//2
    # recursion ending statement
    if ((right_index-left_index) <= s):
        hybridinsertion_sort(array, left_index, right_index)
        return
    else:
        # recursive call 1
        hybrid_sort(array, left_index, middle, s)
        # recurive call 2
        hybrid_sort(array, middle + 1, right_index, s)

    # merging the returned arrays after recurrsion
    merge(array, left_index, right_index, middle)


compares = 0
@st.cache
def perform_mergesorting(data):
    global compares
    comparisons = []
    for x in range(len(data)):
        compares = 0
        merge_sort(data[x], 0, len(data[x])-1)
        comparisons.append(compares)
    return comparisons

compares = 0

@st.cache
def perform_hybridsorting(data, s):
    
    global compares
    
    comparisons = []
    for x in range(len(data)):
        compares = 0
        hybrid_sort(data[x], 0, len(data[x])-1, s)
        comparisons.append(compares)
    return comparisons


def variable_s_hybridsorting(n):
    answer=[]
    x=list(range(1,17))
    x.extend([20,30,40,50,60,70,80,90,100])
    for s in x:
        data=generaterandom_2(n)
        result=perform_hybridsorting(data,s)
        answer.append(Average(result))
    return answer
        
def Average(lst):
    return sum(lst) / len(lst)


st.set_page_config(
    page_title="Interactive Hybrid Sort Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)
#st.info("Note: My main data source, covidtracking.com, has shut down their operation. The data here was last updated March 7, 2021.")
st.title('Interactive Hybrid Sort Dashboard')

# =-----------sidebar---------------_#
st.sidebar.title("FILTER FOR SORTING 📈📊")
st.sidebar.info("Select various values of 'N' and 'S' ")
st.sidebar.text("""
                N : Refers to size of list 
                S : Refers to threshold value 
                
                Use the slider to visualize 
                key comparisons 
                """)
st.sidebar.markdown("#### N (List Size) ")
n = st.sidebar.slider(" ", min_value=100, max_value=10000, value=100)

st.sidebar.markdown("#### S (Threshold) ")
s = st.sidebar.slider(" ", min_value=1, max_value=100, value=5)


# loading data
data_load_state = st.text(
    "Generating randomly generated list of size : " + str(n)+" .....")
data = generaterandom(n)
data_load_state.text('Generating....done!')
# st.dataframe(data)

st.info(""" 
        Value of **N (list size):**
        """
        + str(n) +
        """
        
        Value of **S (Threshold):** 
            """
        + str(s))

# st.write(pd.array(data.loc[1]))

#---- perfrom sorting ------------#
with st.expander('Click to see code for HybridSort'):
    st.code("""
def hybrid_sort(array, left_index, right_index,s):
    # recursion ending statement
    global compares
    if right_index-left_index <= s:
        hybridinsertion_sort(array,left_index,right_index)
        return
    
    # finding middle
    middle = (left_index + right_index)//2
    
    # recursive call 1
    hybrid_sort(array, left_index, middle,s)
    # recurive call 2
    hybrid_sort(array, middle + 1, right_index,s)
    
    # merging the returned arrays after recurrsion
    merge(array, left_index, right_index, middle)
    
    
def merge(array, left_index, right_index, middle):
    
    global compares
    # making copies of list
    left_list=array[left_index:middle+1]
    right_list=array[middle+1:right_index+1]
    
    # intialising indexes
    left_list_index=0
    right_list_index=0
    sorted_index=left_index
    
    
    while(left_list_index<len(left_list) and right_list_index<len(right_list)):
        
        # If left_list has the smaller element, put it in the sorted
        # part and then move forward in left_copy
        if left_list[left_list_index] <= right_list[right_list_index]:
            array[sorted_index] = left_list[left_list_index]
            left_list_index = left_list_index + 1
            #comparison=comparison+1
            compares=compares+1
        # else put the right_list ement in sorted array
        else:
            array[sorted_index] = right_list[right_list_index]
            right_list_index = right_list_index + 1
            compares=compares+1
        
        # increasing sorted index
        sorted_index=sorted_index+1
        
    # Wran out of elemnt in either one of the list
    # so we will put the remaining elements and add them to the sorted list
    while left_list_index < len(left_list):
        array[sorted_index] = left_list[left_list_index]
        left_list_index = left_list_index + 1
        sorted_index = sorted_index + 1
    
    while right_list_index < len(right_list):
        array[sorted_index] = right_list[right_list_index]
        right_list_index = right_list_index + 1
        sorted_index = sorted_index + 1
        
    
def hybridinsertion_sort(array,start,end):
    global compares
    for index in range(start, end+1):
        curr = array[index]
        curr_pos = index
        
        while curr_pos > 0 and array[curr_pos - 1] > curr:
            array[curr_pos] = array[curr_pos -1]
            curr_pos = curr_pos - 1
            compares=compares+1
        array[curr_pos] = curr



            """)

st.markdown('### Running 1000 random list simulations for provided N and S value')

import copy
data_copy = copy.deepcopy(data)
# result=perform_mergesorting(data_2)
# st.table(result)
# st.line_chart(result)

# st.table(data)
result = perform_hybridsorting(data,s)
st.line_chart(result)
# st.table(result)
# st.table(result)
st.balloons()

col1, col2 = st.columns(2)
col1.subheader('Average Key comparisons')
col1.write("""
         **The average key comparisons of all simulations ran :**
         """)
col1.write(Average(result))
col2.subheader('Worst and best cases')
col2.markdown("Best Case : " + str(min(result)))
with col2.expander('Click to see list with best complexity '):
    st.write(data_copy[result.index(min(result))])
    
col2.markdown("Worst Case : " + str(max(result)))
#if(col2.checkbox('Click to see list with worst complexity')):
with col2.expander('Click to see list with worst complexity '):
    st.write(data_copy[result.index(max(result))])
st.markdown(
    '### Keeping N same as provided and runing simulation for variable S(1-32)')

s_result=variable_s_hybridsorting(n)
x=list(range(1,17))
x.extend([20,30,40,50,60,70,80,90,100])
chart_data = pd.DataFrame(
    s_result,
    columns=["Key comparisons"])
chart_data.set_index(pd.Index(x),inplace=True)
#st.dataframe(chart_data)
st.line_chart(chart_data)
st.text_area('Feedback')