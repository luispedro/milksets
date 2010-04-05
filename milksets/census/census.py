# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010, Luis Pedro Coelho <lpc@cmu.edu>
# Software Distributed under the MIT License

from __future__ import division
import numpy as np
from os.path import dirname
import gzip
from ..utils import standard_properties, standard_classification_loader
from ..vtypes import *

__all__ = ['load'] + standard_properties

name = 'Census Income'
short_name = 'Censue'
long_name = 'UCI Census Income'
reference = '''\
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Census-Income+(KDD)'
data_source = 'UCI'
label_names = ['-50000','50000+']
missing_values = True
value_types = [
    continuous('age'),
    categorical('class of worker', ['Not in universe', 'Federal government', 'Local government', 'Never worked', 'Private', 'Self-employed-incorporated', 'Self-employed-not incorporated', 'State government', 'Without pay']),
    categorical('industry recode', ['0', '40', '44', '2', '43', '47', '48', '1', '11', '19', '24', '25', '32', '33', '34', '35', '36', '37', '38', '39', '4', '42', '45', '5', '15', '16', '22', '29', '31', '50', '14', '17', '18', '28', '3', '30', '41', '46', '51', '12', '13', '21', '23', '26', '6', '7', '9', '49', '27', '8', '10', '20']),
    categorical('occupation', ['0', '12', '31', '44', '19', '32', '10', '23', '26', '28', '29', '42', '40', '34', '14', '36', '38', '2', '20', '25', '37', '41', '27', '24', '30', '43', '33', '16', '45', '17', '35', '22', '18', '39', '3', '15', '13', '46', '8', '21', '9', '4', '6', '5', '1', '11', '7']),
    categorical('education',['Children', '7th and 8th grade', '9th grade', '10th grade', 'High school graduate', '11th grade', '12th grade no diploma', '5th or 6th grade', 'Less than 1st grade', 'Bachelors degree(BA AB BS)', '1st 2nd 3rd or 4th grade', 'Some college but no degree', 'Masters degree(MA MS MEng MEd MSW MBA)', 'Associates degree-occup /vocational', 'Associates degree-academic program', 'Doctorate degree(PhD EdD)', 'Prof school degree (MD DDS DVM LLB JD)']),
    continuous('wage per hour'),
    categorical('enrolled in education last week',['Not in universe', 'High school', 'College or university']),
    categorical('marital status', ['Never married', 'Married-civilian spouse present', 'Married-spouse absent', 'Separated', 'Divorced', 'Widowed', 'Married-A F spouse present']),
    categorical('major industry code', [ 'Not in universe or children', 'Entertainment', 'Social services', 'Agriculture', 'Education', 'Public administration', 'Manufacturing-durable goods', 'Manufacturing-nondurable goods', 'Wholesale trade', 'Retail trade', 'Finance insurance and real estate', 'Private household services', 'Business and repair services', 'Personal services except private HH', 'Construction', 'Medical except hospital', 'Other professional services', 'Transportation', 'Utilities and sanitary services', 'Mining', 'Communications', 'Hospital services', 'Forestry and fisheries', 'Armed Forces']),
    categorical('major occupation code', ['Not in universe', 'Professional specialty', 'Other service', 'Farming forestry and fishing', 'Sales', 'Adm support including clerical', 'Protective services', 'Handlers equip cleaners etc', 'Precision production craft & repair', 'Technicians and related support', 'Machine operators assmblrs & inspctrs', 'Transportation and material moving', 'Executive admin and managerial', 'Private household services', 'Armed Forces']),
    categorical('race', ['White', 'Black', 'Other', 'Amer Indian Aleut or Eskimo', 'Asian or Pacific Islander']),
    categorical('hispanic origin', ['Mexican (Mexicano)', 'Mexican-American', 'Puerto Rican', 'Central or South American', 'All other', 'Other Spanish', 'Chicano', 'Cuban', 'Do not know', 'NA']),
    categorical('sex', ['Female', 'Male']),
    categorical('member of a labor union', ['Not in universe', 'No', 'Yes']),
    categorical('reason for unemployment', ['Not in universe', 'Re-entrant', 'Job loser - on layoff', 'New entrant', 'Job leaver', 'Other job loser']),
    categorical('full or part time employment stat', ['Children or Armed Forces', 'Full-time schedules', 'Unemployed part- time', 'Not in labor force', 'Unemployed full-time', 'PT for non-econ reasons usually FT', 'PT for econ reasons usually PT', 'PT for econ reasons usually FT']),
    continuous('capital gains'),
    continuous('capital losses'),
    continuous('dividends from stocks'),
    categorical('tax filer stat', ['Nonfiler', 'Joint one under 65 & one 65+', 'Joint both under 65', 'Single', 'Head of household', 'Joint both 65+']),
    categorical('region of previous residence', ['Not in universe', 'South', 'Northeast', 'West', 'Midwest', 'Abroad']),
    categorical('state of previous residence', ['Not in universe', 'Utah', 'Michigan', 'North Carolina', 'North Dakota', 'Virginia', 'Vermont', 'Wyoming', 'West Virginia', 'Pennsylvania', 'Abroad', 'Oregon', 'California', 'Iowa', 'Florida', 'Arkansas', 'Texas', 'South Carolina', 'Arizona', 'Indiana', 'Tennessee', 'Maine', 'Alaska', 'Ohio', 'Montana', 'Nebraska', 'Mississippi', 'District of Columbia', 'Minnesota', 'Illinois', 'Kentucky', 'Delaware', 'Colorado', 'Maryland', 'Wisconsin', 'New Hampshire', 'Nevada', 'New York', 'Georgia', 'Oklahoma', 'New Mexico', 'South Dakota', 'Missouri', 'Kansas', 'Connecticut', 'Louisiana', 'Alabama', 'Massachusetts', 'Idaho', 'New Jersey']),
    categorical('detailed household and family stat', ['Child <18 never marr not in subfamily', 'Other Rel <18 never marr child of subfamily RP', 'Other Rel <18 never marr not in subfamily', 'Grandchild <18 never marr child of subfamily RP', 'Grandchild <18 never marr not in subfamily', 'Secondary individual', 'In group quarters', 'Child under 18 of RP of unrel subfamily', 'RP of unrelated subfamily', 'Spouse of householder', 'Householder', 'Other Rel <18 never married RP of subfamily', 'Grandchild <18 never marr RP of subfamily', 'Child <18 never marr RP of subfamily', 'Child <18 ever marr not in subfamily', 'Other Rel <18 ever marr RP of subfamily', 'Child <18 ever marr RP of subfamily', 'Nonfamily householder', 'Child <18 spouse of subfamily RP', 'Other Rel <18 spouse of subfamily RP', 'Other Rel <18 ever marr not in subfamily', 'Grandchild <18 ever marr not in subfamily', 'Child 18+ never marr Not in a subfamily', 'Grandchild 18+ never marr not in subfamily', 'Child 18+ ever marr RP of subfamily', 'Other Rel 18+ never marr not in subfamily', 'Child 18+ never marr RP of subfamily', 'Other Rel 18+ ever marr RP of subfamily', 'Other Rel 18+ never marr RP of subfamily', 'Other Rel 18+ spouse of subfamily RP', 'Other Rel 18+ ever marr not in subfamily', 'Child 18+ ever marr Not in a subfamily', 'Grandchild 18+ ever marr not in subfamily', 'Child 18+ spouse of subfamily RP', 'Spouse of RP of unrelated subfamily', 'Grandchild 18+ ever marr RP of subfamily', 'Grandchild 18+ never marr RP of subfamily', 'Grandchild 18+ spouse of subfamily RP']),
    categorical('detailed household summary in household', ['Child under 18 never married', 'Other relative of householder', 'Nonrelative of householder', 'Spouse of householder', 'Householder', 'Child under 18 ever married', 'Group Quarters- Secondary individual', 'Child 18 or older']),
#| instance weight: ignore.
    continuous('instance weight'),
    categorical('migration code-change in msa', ['Not in universe', 'Nonmover', 'MSA to MSA', 'NonMSA to nonMSA', 'MSA to nonMSA', 'NonMSA to MSA', 'Abroad to MSA', 'Not identifiable', 'Abroad to nonMSA']),
    categorical('migration code-change in reg', ['Not in universe', 'Nonmover', 'Same county', 'Different county same state', 'Different state same division', 'Abroad', 'Different region', 'Different division same region']),
    categorical('migration code-move within reg', ['Not in universe', 'Nonmover', 'Same county', 'Different county same state', 'Different state in West', 'Abroad', 'Different state in Midwest', 'Different state in South', 'Different state in Northeast']),
    categorical('live in this house 1 year ago', ['Not in universe under 1 year old', 'Yes', 'No']),
    categorical('migration prev res in sunbelt', ['Not in universe', 'Yes', 'No']),
    continuous('num persons worked for employer'),
    categorical('family members under 18', ['Both parents present', 'Neither parent present', 'Mother only present', 'Father only present', 'Not in universe']),
    categorical('country of birth father', ['Mexico', 'United-States', 'Puerto-Rico', 'Dominican-Republic', 'Jamaica', 'Cuba', 'Portugal', 'Nicaragua', 'Peru', 'Ecuador', 'Guatemala', 'Philippines', 'Canada', 'Columbia', 'El-Salvador', 'Japan', 'England', 'Trinadad&Tobago', 'Honduras', 'Germany', 'Taiwan', 'Outlying-U S (Guam USVI etc)', 'India', 'Vietnam', 'China', 'Hong Kong', 'Cambodia', 'France', 'Laos', 'Haiti', 'South Korea', 'Iran', 'Greece', 'Italy', 'Poland', 'Thailand', 'Yugoslavia', 'Holand-Netherlands', 'Ireland', 'Scotland', 'Hungary', 'Panama']),
    categorical('country of birth mother', ['India', 'Mexico', 'United-States', 'Puerto-Rico', 'Dominican-Republic', 'England', 'Honduras', 'Peru', 'Guatemala', 'Columbia', 'El-Salvador', 'Philippines', 'France', 'Ecuador', 'Nicaragua', 'Cuba', 'Outlying-U S (Guam USVI etc)', 'Jamaica', 'South Korea', 'China', 'Germany', 'Yugoslavia', 'Canada', 'Vietnam', 'Japan', 'Cambodia', 'Ireland', 'Laos', 'Haiti', 'Portugal', 'Taiwan', 'Holand-Netherlands', 'Greece', 'Italy', 'Poland', 'Thailand', 'Trinadad&Tobago', 'Hungary', 'Panama', 'Hong Kong', 'Scotland', 'Iran']),
    categorical('bright country', ['United-States', 'Mexico', 'Puerto-Rico', 'Peru', 'Canada', 'South Korea', 'India', 'Japan', 'Haiti', 'El-Salvador', 'Dominican-Republic', 'Portugal', 'Columbia', 'England', 'Thailand', 'Cuba', 'Laos', 'Panama', 'China', 'Germany', 'Vietnam', 'Italy', 'Honduras', 'Outlying-U S (Guam USVI etc)', 'Hungary', 'Philippines', 'Poland', 'Ecuador', 'Iran', 'Guatemala', 'Holand-Netherlands', 'Taiwan', 'Nicaragua', 'France', 'Jamaica', 'Scotland', 'Yugoslavia', 'Hong Kong', 'Trinadad&Tobago', 'Greece', 'Cambodia', 'Ireland']),
    categorical('citizenship', ['Native- Born in the United States', 'Foreign born- Not a citizen of U S', 'Native- Born in Puerto Rico or U S Outlying', 'Native- Born abroad of American Parent(s)', 'Foreign born- U S citizen by naturalization']),
    categorical('own business or self employed', ['0', '2', '1']),
    categorical('veteran', ['Not in universe', 'Yes', 'No']),
    categorical('veteran benefits', ['0','2','1']),
    continuous('years worked'),
    ordinalrange('year',94,95),
    ]
_datafile = dirname(__file__)+'/data/census-income.data.gz'

@standard_classification_loader(name)
def load(force_contiguous=True):
    features = []
    labels = []
    label_names = [' - 50000.\n',' 50000+.\n']
    for line in gzip.GzipFile(_datafile):
        items = line.split(',')
        cur = []
        for type,val in zip(value_types,items[:-1]):
            val = val.strip()
            if isinstance(type,numeric):
                if val == '?':
                    cur.append(NaN)
                else:
                    cur.append(float(val))
            elif isinstance(type,categorical):
                if val == '?':
                    cur.append('')
                else:
                    if val not in type.categories:
                        raise IOError, "milksets.census.load: Unexpected entry for category (got '%s' for category %s)" % (val,type.name)
                    cur.append(val)
            else:
                raise IOError, "milksets.census.load: Cannot parse file"
        features.append(cur)
        labels.append(label_names.index(items[-1]))
    features = np.array(features)
    labels = np.array(labels)
    return features,labels


