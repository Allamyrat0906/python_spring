from django.shortcuts import render

# Create your views here.


months={
    "january":"test 1",
    "february":"test 2",
    "march":"test 3",
    "april":"test 4",
}
def index(request):
    convert_t_=list(months.keys())
    return render(request, "index.html",{
        "go_to_html":convert_t_
    })
    
def other_temp(request):
    My_name= 'Allamyrat'

    dynamic_data= {"myname": My_name}

    return render(request, "test.html",dynamic_data)


def dynamic_name(request,name):

    data_name={"data_name":name}

    return render(request, "test.html",data_name)

def allMonths(request):
    allM=list(months.keys())
    return render(request,"months.html",
                  {
                      "months":allM
                  })
def valueMonths(request,m):
    #valueMonths=list(months.keys())
    get_data=months[m]
    return render(request,"months.html",
           {
               "get_data":get_data,
               "m_name":m
           })