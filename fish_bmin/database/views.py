from tkinter import S
from urllib import response
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from rest_framework import viewsets, mixins
from django.db.models import Q
from .models import Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier, Resultss
from. serializers import CollectionDateSerializer, Collectorserializer, FamilySerializer, IdentifierSerializer, LocationSerializer, PhotographerSerializer, Preparation1Serializer, Preparation2Serializer, ResultsSerializer, SpecimenSerializer, StatusSerializer, TissueSerializer, ResultsSerializer


class CollectionDateView(viewsets.ModelViewSet):
    queryset = Collection_Date.objects.all()
    serializer_class = CollectionDateSerializer

class CollectorView(viewsets.ModelViewSet):
    queryset = Collector.objects.all()
    serializer_class = Collectorserializer

class FamilyView(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class IdentifierView(viewsets.ModelViewSet):
    queryset = Identifier.objects.all()
    serializer_class = IdentifierSerializer   

class LocationView(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer

class PhotographerView(viewsets.ModelViewSet):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

class Preparation1View(viewsets.ModelViewSet):
    queryset = Preparation1.objects.all()
    serializer_class = Preparation1Serializer

class Preparation2View(viewsets.ModelViewSet):
    queryset = Preparation2.objects.all()
    serializer_class = Preparation2Serializer         

class SpecimenView(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer  

class TissueView(viewsets.ModelViewSet):
    queryset = Tissue.objects.all()
    serializer_class = TissueSerializer

class ResultsView(viewsets.ModelViewSet):
    queryset = Resultss.objects.all()
    serializer_class = ResultsSerializer    

# def home(request):
#     specimen = Specimen.objects.all()

#     context = {''}

# class SearchResultsView(ListView):
#     model = Specimen
#     template_name = 'search.html'

#     def get_queryset(self):
#             query = self.GET.get('Submit')
#             query = str(query)

#             if query is not None:
#                 specimen_set = Specimen.objects.all()

#                 for s in specimen_set:
#                     initial = s.initial_ID
#                     collection_code = s.collection_code
#                     specimen = str(s.dna_barcode)
                    
#                     initial, identity = needle(query, specimen, initial)

#                     # print(identity)

#                     try:
#                         results = Resultss.objects.get(id=s.pk)

#                     except Resultss.DoesNotExist:
#                         results= Resultss(id=s.pk)

#                     identity = str(identity)

#                     results.collection_code = collection_code
#                     results.initial = initial
#                     results.identity = identity

#                     results.save()
            
#                     specimen_list = [collection_code, initial, identity]
#                     results = specimen_list

#                     # print(results)

#             else:
#                 pass

#             results = Resultss.objects.all()

#             allfilter = Resultss.objects.all().order_by('-identity')
            
#             context = {
#                 'results' : allfilter
#             }
        
#             return render(self, 'search.html', context)

# class SearchResultsView(ListView):
#     model = Specimen
#     template_name = 'search.html'

def get_queryset(request):
        query = request.GET.get('query')
        query = str(query)

        if query is not None:
            specimen_set = Specimen.objects.all()

            for specimen in specimen_set:
                s = specimen.pk
                initial = specimen.initial_ID
                collection_code = specimen.collection_code
                location = str(specimen.location)
                specimen = str(specimen.dna_barcode)

                initial, identity = needle(query, specimen, initial)

                try:
                    results = Resultss.objects.get(id=s)

                except Resultss.DoesNotExist:
                    results= Resultss(id=s)

                    identity = str(identity)

                results.collection_code = collection_code
                results.initial = initial
                results.identity = identity
                results.location = location

                results.save()

                specimen_list = [collection_code, initial, identity]
                # results = specimen_list

                print(results)

        else:
            pass

        results = Resultss.objects.all()

        allfilter = Resultss.objects.all().order_by('-identity')
        paginator = Paginator(allfilter, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'results' : allfilter,
            'page_obj' : page_obj,
            'page_number' : page_number
            }

        return render(request, 'search1.html', context)

#This software is a free software. Thus, it is licensed under GNU General Public License.
#Python implementation to Needleman-Wunsch Algorithm for Homework 1 of Bioinformatics class.
#Forrest Bao, Sept. 26 <http://fsbao.net> <forrest.bao aT gmail.com>

# zeros() was origianlly from NumPy.
# This version is implemented by alevchuk 2011-04-10
def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval

match_award      = 10
mismatch_penalty = -5
gap_penalty      = -5 # both for opening and extanding

def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty

def finalize(align1, align2):
    align1 = align1[::-1]    #reverse sequence 1
    align2 = align2[::-1]    #reverse sequence 2
    
    i,j = 0,0
    
    #calcuate identity, score and aligned sequeces
    symbol = ''
    found = 0
    score = 0
    identity = 0
    for i in range(0,len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:                
            symbol = symbol + align1[i]
            identity = identity + 1
            score += match_score(align1[i], align2[i])
    
        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-': 
            score += match_score(align1[i], align2[i])
            symbol += ' '
            found = 0
    
        #if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':          
            symbol += ' '
            score += gap_penalty
    
    identity = float(identity) / len(align1) * 100
    identity = round(identity, 3)

    # print ('Identity =', "%3.3f" % identity, 'percent')
    # print ('Score =', score)
    # print ('This is align1 = ' , align1)
    # print ('This is symbol = ', symbol)
    # print ('This is align2 = ', align2)

    return identity, align2, score
    
    
def needle(seq1, seq2, initial):
    m, n = len(seq1), len(seq2)  # length of two sequences
    
    # Generate DP table and traceback path pointer matrix
    score = zeros((m+1, n+1))      # the DP table
   
    # Calculate DP table
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment 
    align1, align2 = '', ''
    i,j = m,n # start from the bottom right cell
    while i > 0 and j > 0: # end toching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]

        if score_current == score_diagonal + match_score(seq1[i-1], seq2[j-1]):
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1

    # Finish tracing up to the top left cell
    while i > 0:
        align1 += seq1[i-1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j-1]
        j -= 1

    identity, align2, score = finalize(align1, align2)
    
    return initial, identity

    
    

    