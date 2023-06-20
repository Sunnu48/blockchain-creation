
"""
Python Programming (ACFI827)
Assignment1 Submission
Sunit Kumar
ID: 201622891
"""

#importing libraries that we are going to use in our Assignment
import hashlib as _hashlib
import random
import datetime
import json as _json
import time
import sys


print("Press 1 to see full assignment TASK-wise or Press 2 to see Execution Time of assignment")
while True:

    try:
        n=int(input())
    except ValueError:#handling input error for integer
        print("Please Enter a Valid Number 1 or 2")
        continue
    try:
        if(n!=1 and n!=2 ):
            raise TypeError("Please Enter either 1 or 2 to choose mode")
    except TypeError as a:#handling input error if input is not 1 or 2
            print(a)
    else:
        break
pass
start=time.time()



print("-----------------------------------------------------------------------Assignment 1-----------------------------------------------------------------------------------")
"""**READING JSON FILE**"""

jsonFilePath = r'political-emails.json'  #This is the Path of the file

try:
    with open(jsonFilePath) as json_file:  #Opening json file in python
        json_data = _json.load(json_file)
except IOError:#handling error in json file
      print("Error: File does not appear to exist.")
      sys.exit()


###########################################################################################################
def press_ENTER(msg): #Function to take "Enter Key" as Input from User to Execute output TASK by TASK
    while True:
        try:
            i=input(msg)
            if(i!=""):
                raise ValueError("You Pressed the wrong key before pressing Enter")
        except ValueError as e:#handling input error if enter is not pressed
            print(e)
        else:
            del(i)
            break
    pass
##########################################################################################################
"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                     #TASK A
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Find the number of political emails in the dataset.
"""

if(n==1):
    press_ENTER("   Press 'Enter' to execute Task A    ")
print("--Total no of Emails in Political EmailFail are ",len(json_data))
print()

l=[]
l.extend(list(json_data[0].keys()))
flag=0
for i in range(1,len(json_data)):
    d=list(json_data[i].keys())
    if(l!=d):
        flag=1
        print("--Keys are different")
        break

if(flag==0):
    print('--All keys are identitical')
print()

"""###########################--------------TaskA-----------------###############################completed"""


"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                     #TASK B
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def hash(block):
    # to do hashing of a block since it is a dictionary
    encoded_block = str(block).encode()
    hashvalue = _hashlib.sha256(encoded_block).hexdigest()
    return hashvalue

if(n==1):
    #print("   Press 'Enter' to execute Task B    ")
    press_ENTER("   Press 'Enter' to execute Task B    ")
print()

#1 Create a hash value of 9th email and assign it to variable hashvalue1.

hashvalue1 = hash(json_data[8])
print("hashvalue1-- ",hashvalue1)

#Create another hash value of 9th email and assign it to variable hashvalue2.
hashvalue2 = hash(json_data[8])
print("hashvalue2-- ",hashvalue2)

#Create a hash value of 11th email and assign it to variable hashvalue3.
hashvalue3=hash(json_data[10])
print("hashvalue3-- ",hashvalue3)

if(hashvalue1==hashvalue2):
    print("--hashvalue1 and hashvalue2 are identical")
else:
    print("-- hashvalue1 and hashvalue2 are different")

if(hashvalue1==hashvalue3):
    print("--hashvalue1 and hashvalue3 are identical")
else:
    print("--hashvalue1 and hashvalue3 are different")
print()


"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                     #TASK C
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
if(n==1):
    press_ENTER("   Press 'Enter' to execute Task C   ")
print()
chain=[]
def create_block(s=0,proof=1,pref_hash=hash('000')):
    block={'block_index': len(chain)+1,
        'transaction_timestamp': str(datetime.datetime.now()),
        'transaction_data': "This is the genesis block of email transaction" if proof==1 and pref_hash==hash('000')
        else json_data[s]['datetime'] + ", " + json_data[s]['email_id'], # checking if the value passed as arguments
           # are default or not, if so then execute genesis block else create a new block
        'proof_of_work': proof,
        'previous_hash': pref_hash}
    #create_chain(block)
    return block


def create_chain(block):
    chain.append(block)

#---------------------------------TASK C1 and C2-----------------------------------------------------------


def proof_of_work(prev_proof):
    # proof of work requires for mining of block
    new_proof = 1
    check_proof = False
    #Here we taking an Easy Proof of work Algorithm equation for less computation time
    #since the equation containing previous proof and new proof has to be asymmetric so
    while check_proof is False:
        hash_op = _hashlib.sha256(str(new_proof ** 2 - prev_proof ** 3).encode()).hexdigest()
        if hash_op[:3] == '000':
            check_proof = True
        else:
            new_proof += 1
    return new_proof

def mine_block(s):
    if(len(chain)==0):#TO check is our blokchain contains a genesis block or not before adding a block
        create_chain(create_block())#creating a genesis block
    previoushash=hash(chain[-1])
    proofofwork = proof_of_work(chain[-1]['proof_of_work'])
    block=create_block(s,proofofwork,previoushash)
    create_chain(block)
    #print("The email id {} is added to block".format(json_data[s]['email_id']))

#-------------------------------------------TASK C3--------------------------------------------------------

i=0
print("--",end='')
while(i<120):
    s=random.randint(0,405)
    mine_block(s)
    i+=1
print("A Blockchain is Created with Random 120 emails from political email data")
print()
if(n==1):
    press_ENTER("   Press 'Enter' to see the Blockchain   ")
    for each_ele in chain:
        print(each_ele)
    checking=[]
    for n in chain:
        if(n['proof_of_work'] not in checking):
            checking.append(n['proof_of_work'])
        else:
            print(chain.index(n['proof_of_work']))
            print("same")
            break
        #print(n[proof_of_work()])
    print("--The length of blockchain is ",len(chain))
#print(chain)

#-------------------------------TASK_C4----------------------------------------------------------------------
print()
if(n==2):
    print("--Execution time is ",time.time()-start)
    exit("Thank you")
else:
    press_ENTER("Press 'Enter' to exit")
    exit("Thank you")


#--------------------------------------------------------------------------------------------------------------
#                                          OUTPUT
#--------------------------------------------------------------------------------------------------------------

"""
Press 1 to see full assignment TASK-wise or Press 2 to see Execution Time of assignment
1
-----------------------------------------------------------------------Assignment 1-----------------------------------------------------------------------------------
   Press 'Enter' to execute Task A    
--Total no of Emails in Political EmailFail are  406

--All keys are identitical

   Press 'Enter' to execute Task B    

hashvalue1--  a2981b38880b19db5eaaa6dd70a80f5fb85cffcb4e2e72171d2dff6f57dfa7b2
hashvalue2--  a2981b38880b19db5eaaa6dd70a80f5fb85cffcb4e2e72171d2dff6f57dfa7b2
hashvalue3--  f48a77fb8a999126bb84054a70f2fdb9bfaa474ce1fd5267fab74dbed22c643c
--hashvalue1 and hashvalue2 are identical
--hashvalue1 and hashvalue3 are different

   Press 'Enter' to execute Task C   

--
A Blockchain is Created with Random 120 emails from political email data

   Press 'Enter' to see the Blockchain   {'block_index': 1, 'transaction_timestamp': '2022-12-11 16:37:35.715959', 'transaction_data': 'This is the genesis block of email transaction', 'proof_of_work': 1, 'previous_hash': '2ac9a6746aca543af8dff39894cfe8173afba21eb01c6fae33d52947222855ef'}
{'block_index': 2, 'transaction_timestamp': '2022-12-11 16:37:35.718914', 'transaction_data': '14/12/2019 12:52, 119', 'proof_of_work': 533, 'previous_hash': '0a1a89857dd1f3b2d105e322a7607614f17ba959ded237aa4bee2dd14f20b9e8'}
{'block_index': 3, 'transaction_timestamp': '2022-12-11 16:37:35.754813', 'transaction_data': '15/12/2017 07:28, 404', 'proof_of_work': 6809, 'previous_hash': 'e60c70d93589ae8080622d2b709a511fd84b4808014be4015b59b1266f3bfd70'}
{'block_index': 4, 'transaction_timestamp': '2022-12-11 16:37:35.761795', 'transaction_data': '03/06/2020 13:40, 348', 'proof_of_work': 1814, 'previous_hash': 'dcb6c32caafa4e7134f0fe93085d98c5954737dc96f46a0fd3c00f25e025663c'}
{'block_index': 5, 'transaction_timestamp': '2022-12-11 16:37:35.769773', 'transaction_data': '07/01/2019 06:56, 57', 'proof_of_work': 1965, 'previous_hash': '5fba9d4a04982067c09345a7f5a5ab08cfe08e010a91dc779d8c4fc7127452a1'}
{'block_index': 6, 'transaction_timestamp': '2022-12-11 16:37:35.776793', 'transaction_data': '07/11/2019 07:10, 108', 'proof_of_work': 1774, 'previous_hash': '890901a62cf1b45c34ba07068b65fedfaf851c341eb552b6e62875f6893c693b'}
{'block_index': 7, 'transaction_timestamp': '2022-12-11 16:37:35.789758', 'transaction_data': '14/08/2019 15:59, 286', 'proof_of_work': 3162, 'previous_hash': 'ebd1d0bb309c0fe38c0c9ce2b05ad69915f80031b80a1d95fc802b26364eb194'}
{'block_index': 8, 'transaction_timestamp': '2022-12-11 16:37:35.789758', 'transaction_data': '26/02/2020 14:02, 325', 'proof_of_work': 178, 'previous_hash': '6ce598c2e86df01f7dc0737bb725562f6a5c0ef2978fc3e95fde2eb708e35cfc'}
{'block_index': 9, 'transaction_timestamp': '2022-12-11 16:37:35.803721', 'transaction_data': '21/06/2019 12:59, 275', 'proof_of_work': 3631, 'previous_hash': 'c9982327bbcfad8f381ae7a72a72b7e419e95b9cdd31d3ea6f204436762a700a'}
{'block_index': 10, 'transaction_timestamp': '2022-12-11 16:37:35.808707', 'transaction_data': '11/02/2020 17:36, 132', 'proof_of_work': 1211, 'previous_hash': 'df9a01cd5f271271376264711fdbea08742ce00f885a10479bb120332ed4ecb8'}
{'block_index': 11, 'transaction_timestamp': '2022-12-11 16:37:35.809704', 'transaction_data': '28/06/2018 15:43, 28', 'proof_of_work': 292, 'previous_hash': '547064adadb0b44f5cd28de53e81ed38c932a81de00dc6980e5066ac2ceb32ab'}
{'block_index': 12, 'transaction_timestamp': '2022-12-11 16:37:35.828652', 'transaction_data': '18/06/2018 15:25, 24', 'proof_of_work': 5128, 'previous_hash': '2fb73b124523c1e4035490237d22a61996eb445a06f283a469f0627e151af787'}
{'block_index': 13, 'transaction_timestamp': '2022-12-11 16:37:35.853592', 'transaction_data': '26/04/2019 10:27, 59', 'proof_of_work': 7766, 'previous_hash': '4ce81d812bab2fed25f7b58ae0a44dfb5baf0b0413b17161eeb4c5d38aa97b06'}
{'block_index': 14, 'transaction_timestamp': '2022-12-11 16:37:35.870541', 'transaction_data': '23/10/2018 17:52, 255', 'proof_of_work': 5312, 'previous_hash': 'be789cb3e650df6b65b3b758afeb5ba2fe512d1161d3661d03d4eba9a43b574a'}
{'block_index': 15, 'transaction_timestamp': '2022-12-11 16:37:35.903464', 'transaction_data': '10/07/2020 16:30, 356', 'proof_of_work': 10782, 'previous_hash': '691eeddd35e82e5e6adeed70a5b21cd9ff613c939033d160a272315f880bb488'}
{'block_index': 16, 'transaction_timestamp': '2022-12-11 16:37:35.912449', 'transaction_data': '14/07/2017 12:04, 2', 'proof_of_work': 3066, 'previous_hash': '8f8def768bbe930b523f01742314d1d018f56948e5039998cfe33ffa1c69a46f'}
{'block_index': 17, 'transaction_timestamp': '2022-12-11 16:37:35.930387', 'transaction_data': '09/02/2017 09:22, 301', 'proof_of_work': 6208, 'previous_hash': 'fa6ce1958f24687e1a1e11a5c368e8e04364bc4b3f45ff0487e42632b987d162'}
{'block_index': 18, 'transaction_timestamp': '2022-12-11 16:37:35.936374', 'transaction_data': '12/08/2020 13:12, 193', 'proof_of_work': 1839, 'previous_hash': '2df0190b3a9f0e5bb903f88843ede5a0d6647f37b94b4df7a4ef25361cdb86bc'}
{'block_index': 19, 'transaction_timestamp': '2022-12-11 16:37:35.937370', 'transaction_data': '26/03/2018 09:59, 219', 'proof_of_work': 508, 'previous_hash': '35f3afa7a03253e71b8be73c5eec9ada7717c2f50170ef121ec9f88e86105c8d'}
{'block_index': 20, 'transaction_timestamp': '2022-12-11 16:37:35.940615', 'transaction_data': '12/11/2019 06:44, 109', 'proof_of_work': 857, 'previous_hash': '6c1f176e138bbf32ff916c396e0ca4a8efabd6aa172a79d923f5a991a92ccaf9'}
{'block_index': 21, 'transaction_timestamp': '2022-12-11 16:37:36.008466', 'transaction_data': '22/11/2019 14:04, 309', 'proof_of_work': 21193, 'previous_hash': '5ff72a4b7cfe4e15c14ce47e3da717853a15968635d96085c8a6ff7facaeb276'}
{'block_index': 22, 'transaction_timestamp': '2022-12-11 16:37:36.023386', 'transaction_data': '03/08/2017 17:58, 203', 'proof_of_work': 4702, 'previous_hash': '6ca49db9a0fb4abba0a06368c6c4c6368e70a5ef841c7757056d9f2c62698cd7'}
{'block_index': 23, 'transaction_timestamp': '2022-12-11 16:37:36.044363', 'transaction_data': '13/10/2020 05:03, 383', 'proof_of_work': 6607, 'previous_hash': '30ec6ccb81ececaf0778027c16c25a1ba5c4f10e074f52ec415051c994052b35'}
{'block_index': 24, 'transaction_timestamp': '2022-12-11 16:37:36.064277', 'transaction_data': '24/05/2020 10:40, 346', 'proof_of_work': 5976, 'previous_hash': '3bb4115033efec6fc5ba38900f464f91115668501e0f7622038385d087731b4e'}
{'block_index': 25, 'transaction_timestamp': '2022-12-11 16:37:36.080236', 'transaction_data': '02/10/2019 10:18, 294', 'proof_of_work': 5008, 'previous_hash': '40f28b18f862b6aef15893f151e4d82a3e93153625282834deaca9d772f057f5'}
{'block_index': 26, 'transaction_timestamp': '2022-12-11 16:37:36.082229', 'transaction_data': '15/11/2017 17:38, 400', 'proof_of_work': 600, 'previous_hash': 'a1f0db91a80b6fbf0de3055dc45fa0166c3b997622a4670cfdfec6ee2d33d2f4'}
{'block_index': 27, 'transaction_timestamp': '2022-12-11 16:37:36.093201', 'transaction_data': '29/06/2018 11:10, 29', 'proof_of_work': 3557, 'previous_hash': '510ae7a6b316d3639165804d1324235e7556b5361d709361622508a1526c1a4f'}
{'block_index': 28, 'transaction_timestamp': '2022-12-11 16:37:36.126115', 'transaction_data': '17/10/2017 05:20, 207', 'proof_of_work': 10904, 'previous_hash': 'e20d8649766f82604c1626fd43222a1f08c41a9f6254561d4bcd0e3473c6ffed'}
{'block_index': 29, 'transaction_timestamp': '2022-12-11 16:37:36.138088', 'transaction_data': '31/12/2017 14:04, 10', 'proof_of_work': 3998, 'previous_hash': '26f7c5d7ec6a6e61ccd6d280b4c4e3ddaba6c4bb4c05637e80c1ac10ccb46010'}
{'block_index': 30, 'transaction_timestamp': '2022-12-11 16:37:36.180968', 'transaction_data': '04/07/2020 06:46, 180', 'proof_of_work': 14734, 'previous_hash': 'f8fbcf48c7ab8d2e6d844c32f0a0fbf260bac11a7b80e6b304f5785cdfababa9'}
{'block_index': 31, 'transaction_timestamp': '2022-12-11 16:37:36.183963', 'transaction_data': '04/10/2020 11:53, 381', 'proof_of_work': 705, 'previous_hash': '40182879172275329e9e6abd2373d395d7e763cc28c727ec4a7d8d94bd80c6bf'}
{'block_index': 32, 'transaction_timestamp': '2022-12-11 16:37:36.189944', 'transaction_data': '23/10/2017 12:22, 397', 'proof_of_work': 2124, 'previous_hash': '0eb375a73b85200482ddd9989074415fb4866d21f5654c81f45301bd59b0ef1c'}
{'block_index': 33, 'transaction_timestamp': '2022-12-11 16:37:36.196926', 'transaction_data': '26/04/2020 18:39, 337', 'proof_of_work': 2589, 'previous_hash': '543935c43ef534f4f9585b4268b5b3985c72f48dc05c0b52c6630616eb7f82fe'}
{'block_index': 34, 'transaction_timestamp': '2022-12-11 16:37:36.220862', 'transaction_data': '10/02/2020 16:31, 133', 'proof_of_work': 7972, 'previous_hash': '7a23326b6760bcd9565ed9ba34cfa9395e4f4f776ec6165b77bc2c8323961adc'}
{'block_index': 35, 'transaction_timestamp': '2022-12-11 16:37:36.231845', 'transaction_data': '17/12/2020 08:56, 252', 'proof_of_work': 3838, 'previous_hash': '841d9ddf19bb5d0732451d02a4640905abed938b1cda7417a3c0097179a8de05'}
{'block_index': 36, 'transaction_timestamp': '2022-12-11 16:37:36.240898', 'transaction_data': '14/02/2020 13:00, 134', 'proof_of_work': 2889, 'previous_hash': 'd366c08c9b0ee7bcf9185b3181c7157b981dd2ac084f0d05dee556ed8692e7f9'}
{'block_index': 37, 'transaction_timestamp': '2022-12-11 16:37:36.245794', 'transaction_data': '30/07/2020 08:30, 364', 'proof_of_work': 1598, 'previous_hash': '8d9fd65c15d10d28af60b550c009fc506e6f50589d3fde69c08db14d1015bfbd'}
{'block_index': 38, 'transaction_timestamp': '2022-12-11 16:37:36.256772', 'transaction_data': '15/10/2018 17:13, 47', 'proof_of_work': 3818, 'previous_hash': '8de6f74a352e80c072b4c22745e83f2715749035edea9f1d54e086907ea4204e'}
{'block_index': 39, 'transaction_timestamp': '2022-12-11 16:37:36.258760', 'transaction_data': '23/09/2020 05:05, 379', 'proof_of_work': 596, 'previous_hash': 'f879cf2f7dbadeb901778952d0e5f28141c47efdfb41082d697f37fa94db9cd5'}
{'block_index': 40, 'transaction_timestamp': '2022-12-11 16:37:36.260756', 'transaction_data': '30/12/2017 06:45, 213', 'proof_of_work': 914, 'previous_hash': '3f2d390300b08e37094e17f344b18c0c91e09f041ba38279e77b6216f665bab0'}
{'block_index': 41, 'transaction_timestamp': '2022-12-11 16:37:36.281713', 'transaction_data': '12/02/2018 15:03, 13', 'proof_of_work': 6922, 'previous_hash': 'fcb6c0d98522fce61826559365de538fc4f2106d40f1d8cd6bcec9c442a90d6d'}
{'block_index': 42, 'transaction_timestamp': '2022-12-11 16:37:36.321595', 'transaction_data': '14/02/2020 13:00, 134', 'proof_of_work': 13857, 'previous_hash': '7e5e0a375b23c596e33e0c9a1685ce27bc28713a5ca5540524e4561ec41b1bd2'}
{'block_index': 43, 'transaction_timestamp': '2022-12-11 16:37:36.347524', 'transaction_data': '11/12/2017 06:54, 209', 'proof_of_work': 9002, 'previous_hash': '9596b6b10f9dfe4f1871df61a9090661adffeaafa6f2512ad0203b8526a5ff25'}
{'block_index': 44, 'transaction_timestamp': '2022-12-11 16:37:36.350515', 'transaction_data': '09/05/2020 12:13, 343', 'proof_of_work': 1076, 'previous_hash': '3ce8043195a314895c709abf2cb59a8654a86eb1deeb217d65e1d9a39911196c'}
{'block_index': 45, 'transaction_timestamp': '2022-12-11 16:37:36.355498', 'transaction_data': '18/08/2017 08:04, 204', 'proof_of_work': 1640, 'previous_hash': '66b9c5806170c39f13d6b31e52139187af10b060c09ce26b3bda35f3f75d1a09'}
{'block_index': 46, 'transaction_timestamp': '2022-12-11 16:37:36.378440', 'transaction_data': '06/05/2020 08:08, 159', 'proof_of_work': 7867, 'previous_hash': '320ba3669cd55fc7d28bc383abe4849f53ad3be254461b08e45853b6b81af273'}
{'block_index': 47, 'transaction_timestamp': '2022-12-11 16:37:36.431296', 'transaction_data': '18/05/2020 16:30, 163', 'proof_of_work': 18453, 'previous_hash': '65bfcdee80b10e6b48d6733a9d9ccea81e9fc95f5b4e7369a7578b4d29ff86ea'}
{'block_index': 48, 'transaction_timestamp': '2022-12-11 16:37:36.474182', 'transaction_data': '26/02/2020 18:16, 135', 'proof_of_work': 15044, 'previous_hash': '3e07418750e8a8dba65f43d8c0320ac3102216b361fee7489e3db1d997c63729'}
{'block_index': 49, 'transaction_timestamp': '2022-12-11 16:37:36.540636', 'transaction_data': '15/07/2019 07:52, 77', 'proof_of_work': 19948, 'previous_hash': 'b37bd5a066df39f99ce9f567b09905f6efa39ba22a8f077a4633d08a359390bf'}
{'block_index': 50, 'transaction_timestamp': '2022-12-11 16:37:36.543632', 'transaction_data': '11/11/2019 14:12, 300', 'proof_of_work': 915, 'previous_hash': '8fcf849f2e6b60ebc80d1060fb856b4bf5045b9e441792757e17be2b77296165'}
{'block_index': 51, 'transaction_timestamp': '2022-12-11 16:37:36.555602', 'transaction_data': '27/12/2017 08:07, 406', 'proof_of_work': 4076, 'previous_hash': '84667b5a0cbc9c5f3b83d6446ab1a6bd1d6c3354a0a57ceee85c5625b50b643f'}
{'block_index': 52, 'transaction_timestamp': '2022-12-11 16:37:36.556573', 'transaction_data': '03/05/2017 18:24, 271', 'proof_of_work': 92, 'previous_hash': 'b51105e64d09856ab38bef04ae7037e77823518671405897f19c4d5d8f5f1cc7'}
{'block_index': 53, 'transaction_timestamp': '2022-12-11 16:37:36.556573', 'transaction_data': '04/11/2019 12:43, 107', 'proof_of_work': 171, 'previous_hash': '1f19dfb6e522d3cf4e6d1c405bdfbe3fc60739d98383fd92b2c3876e0ce64703'}
{'block_index': 54, 'transaction_timestamp': '2022-12-11 16:37:36.581630', 'transaction_data': '31/12/2019 18:52, 123', 'proof_of_work': 8284, 'previous_hash': 'a7614e70d23c4763f763a846ce834f6d54f09eef68ab3cf2862cfd241f363606'}
{'block_index': 55, 'transaction_timestamp': '2022-12-11 16:37:36.601653', 'transaction_data': '06/09/2019 11:15, 93', 'proof_of_work': 6759, 'previous_hash': '4664b08a942c513362554419960a2137bf1c36194390dd79996f52ee3505ca2e'}
{'block_index': 56, 'transaction_timestamp': '2022-12-11 16:37:36.613608', 'transaction_data': '02/12/2016 06:20, 307', 'proof_of_work': 4129, 'previous_hash': '1427d2980cc6222be78262d3b7e625efc40f37ad07dd4082fdbea352ea8ff3eb'}
{'block_index': 57, 'transaction_timestamp': '2022-12-11 16:37:36.625619', 'transaction_data': '07/12/2019 09:15, 314', 'proof_of_work': 3804, 'previous_hash': '4448ba7a769c4e8a5e1415630867c58adf921a6270668978a86108b788906307'}
{'block_index': 58, 'transaction_timestamp': '2022-12-11 16:37:36.641578', 'transaction_data': '02/08/2018 13:21, 33', 'proof_of_work': 5208, 'previous_hash': '4d292b3b61b345a80112910733e2fbce3ed94a0ab1bf73f7d89558abc32dd86a'}
{'block_index': 59, 'transaction_timestamp': '2022-12-11 16:37:36.658524', 'transaction_data': '17/09/2019 16:57, 96', 'proof_of_work': 5637, 'previous_hash': '9d0c93836d50075c8935ed0c758e64c77b513da16e140616383fe0db3d87c7f2'}
{'block_index': 60, 'transaction_timestamp': '2022-12-11 16:37:36.666554', 'transaction_data': '15/01/2020 12:04, 321', 'proof_of_work': 2864, 'previous_hash': '1cab2dcb8b99abd6be485d0e86988b3ecbd5d7129a569adcf896f286f4c54aa5'}
{'block_index': 61, 'transaction_timestamp': '2022-12-11 16:37:36.685504', 'transaction_data': '16/07/2018 08:23, 239', 'proof_of_work': 6505, 'previous_hash': '67dcedc01a91f239f840b0b4a2e2a019572cd9afa23b17e1a0d2cab6be1c42f6'}
{'block_index': 62, 'transaction_timestamp': '2022-12-11 16:37:36.685504', 'transaction_data': '28/02/2020 11:25, 327', 'proof_of_work': 182, 'previous_hash': '92b152785bf1bd9f4801ddd9cf14a4b176912621d15d1c20d74ac3a1d323c4ed'}
{'block_index': 63, 'transaction_timestamp': '2022-12-11 16:37:36.697452', 'transaction_data': '15/05/2019 14:29, 61', 'proof_of_work': 3900, 'previous_hash': '2390e304f9bf868b650078e328348297078a4c6114bb83651a69cbb6078fca3e'}
{'block_index': 64, 'transaction_timestamp': '2022-12-11 16:37:36.699450', 'transaction_data': '18/09/2019 07:52, 291', 'proof_of_work': 538, 'previous_hash': '2b3f317a30d0dd71371806d8eeddc68148c0de4eafe0930e4658346d15744d38'}
{'block_index': 65, 'transaction_timestamp': '2022-12-11 16:37:36.720394', 'transaction_data': '08/05/2020 11:36, 160', 'proof_of_work': 7458, 'previous_hash': 'abbc44c3bef67ffd00c289db6685a9c4ee67c8fc7f6df3d4bb4c5806b0a3a455'}
{'block_index': 66, 'transaction_timestamp': '2022-12-11 16:37:36.740338', 'transaction_data': '27/12/2017 08:07, 406', 'proof_of_work': 6762, 'previous_hash': '9c7b1aea8f4d46996025d56bfc19fb72f5dcdc6d4a730d9ea6ea5a5f42dfef8d'}
{'block_index': 67, 'transaction_timestamp': '2022-12-11 16:37:36.753303', 'transaction_data': '17/08/2018 07:18, 245', 'proof_of_work': 4306, 'previous_hash': 'e9605db367123ae237c971749b09d9485245997a69146d7166579ee3ff21a54a'}
{'block_index': 68, 'transaction_timestamp': '2022-12-11 16:37:36.771268', 'transaction_data': '05/08/2020 13:56, 192', 'proof_of_work': 6410, 'previous_hash': '4725b2769bf426173ffa0e9e09cfbf07d8a61e530389961c0946610370abc8b0'}
{'block_index': 69, 'transaction_timestamp': '2022-12-11 16:37:36.773249', 'transaction_data': '18/08/2017 08:04, 204', 'proof_of_work': 663, 'previous_hash': '669008c50f995657c3510e75917d30f8887f233e506eba1b408f25ffda2f51d1'}
{'block_index': 70, 'transaction_timestamp': '2022-12-11 16:37:36.779235', 'transaction_data': '06/09/2018 15:38, 40', 'proof_of_work': 2080, 'previous_hash': '4b7c45b5c8a75aebf0b89241edf187bc715d72f204dd365aa91283236b627b94'}
{'block_index': 71, 'transaction_timestamp': '2022-12-11 16:37:36.779235', 'transaction_data': '12/08/2020 13:12, 193', 'proof_of_work': 75, 'previous_hash': 'f98266f1b320554048459836955df254f4b7365938f879c6a7522ab0c2f639ba'}
{'block_index': 72, 'transaction_timestamp': '2022-12-11 16:37:36.786215', 'transaction_data': '13/06/2018 12:01, 23', 'proof_of_work': 2319, 'previous_hash': '302e5481a79bc6a172f5d1883d8abcc8eed0f45cc50ce20e7f14339485a278f1'}
{'block_index': 73, 'transaction_timestamp': '2022-12-11 16:37:36.792199', 'transaction_data': '15/01/2020 12:04, 321', 'proof_of_work': 2133, 'previous_hash': '592968fce757980c214e36f2c7a87a41c9707dfd898bc3b2bdd96bdb68fea937'}
{'block_index': 74, 'transaction_timestamp': '2022-12-11 16:37:36.806165', 'transaction_data': '07/05/2020 06:39, 161', 'proof_of_work': 4812, 'previous_hash': 'cfa04ec6dafaa5be95e3b17fc96028476c9152c6bb0006117d9cb048367b6bf2'}
{'block_index': 75, 'transaction_timestamp': '2022-12-11 16:37:36.821136', 'transaction_data': '04/03/2020 06:52, 138', 'proof_of_work': 5011, 'previous_hash': 'bbf17bc84ba197d1c27cfc3a5003df8d3eac80287dedbe539929fbb92475adae'}
{'block_index': 76, 'transaction_timestamp': '2022-12-11 16:37:36.824114', 'transaction_data': '12/06/2020 13:01, 351', 'proof_of_work': 996, 'previous_hash': '17fa864af7607cf16dfbd1fa8c50d06e54499a50546eac15ecd39699e993e165'}
{'block_index': 77, 'transaction_timestamp': '2022-12-11 16:37:36.827105', 'transaction_data': '28/02/2020 11:25, 327', 'proof_of_work': 980, 'previous_hash': '7e22efd38a0e604cbdcf0dbaf50ae38e18e92171d15fdce0b904acbf0a562306'}
{'block_index': 78, 'transaction_timestamp': '2022-12-11 16:37:36.843063', 'transaction_data': '27/11/2019 18:29, 311', 'proof_of_work': 5930, 'previous_hash': '75b56dfad71db916028f4feae7be3429936eca738edf604b62622de83cab9c62'}
{'block_index': 79, 'transaction_timestamp': '2022-12-11 16:37:36.845058', 'transaction_data': '04/07/2020 13:03, 179', 'proof_of_work': 483, 'previous_hash': 'e731c3d9127c24ed672956f63779fb305ba0f795df9c3675ebef7a9c2e7358ce'}
{'block_index': 80, 'transaction_timestamp': '2022-12-11 16:37:36.847051', 'transaction_data': '12/10/2018 17:04, 46', 'proof_of_work': 618, 'previous_hash': '8d2f85e11dcb4e3bc9721bb614d0bd97926921664b23c99cb381002455606bae'}
{'block_index': 81, 'transaction_timestamp': '2022-12-11 16:37:36.872982', 'transaction_data': '21/09/2020 10:48, 378', 'proof_of_work': 9129, 'previous_hash': 'a6ac005303ffd9050f873398d1b0a8e8e2e16d8279a58c1a5adc8105441b4e64'}
{'block_index': 82, 'transaction_timestamp': '2022-12-11 16:37:36.876971', 'transaction_data': '20/10/2016 07:47, 184', 'proof_of_work': 1414, 'previous_hash': 'f40c6e885b231033c677fa5cab09432909a59a62a04b8bcbefa4084802a15f79'}
{'block_index': 83, 'transaction_timestamp': '2022-12-11 16:37:36.883953', 'transaction_data': '03/05/2019 12:20, 267', 'proof_of_work': 2289, 'previous_hash': '25954fe2b7e1e19cb2601237237efbc62d7ebf7f46fa8d49fffce42996e47742'}
{'block_index': 84, 'transaction_timestamp': '2022-12-11 16:37:36.890947', 'transaction_data': '17/10/2017 05:20, 207', 'proof_of_work': 2395, 'previous_hash': '9eeb3a033c5233c9eef8a0c5e3bdcab2c1fbc79a5661a218f897e0a2cad48794'}
{'block_index': 85, 'transaction_timestamp': '2022-12-11 16:37:36.913876', 'transaction_data': '23/09/2020 05:05, 379', 'proof_of_work': 8011, 'previous_hash': '015bc2d5a0b10f57adfd1a4510aced57df774e19a8fe0c7db5caf3cb55bed59d'}
{'block_index': 86, 'transaction_timestamp': '2022-12-11 16:37:36.916864', 'transaction_data': '26/07/2017 14:23, 393', 'proof_of_work': 1201, 'previous_hash': '1108017bc49ee20d5d4a2fba1ceb5c0ca6536261e92b5fc539edab8c6030b0c1'}
{'block_index': 87, 'transaction_timestamp': '2022-12-11 16:37:36.928833', 'transaction_data': '14/07/2020 16:00, 357', 'proof_of_work': 4180, 'previous_hash': '11948be53fac0f0940e1cc16f14e56f5c8d44cdc239f4ff0a4b3d4c12496f01d'}
{'block_index': 88, 'transaction_timestamp': '2022-12-11 16:37:36.938806', 'transaction_data': '06/09/2020 06:25, 199', 'proof_of_work': 3241, 'previous_hash': '42d3641347d58d1da37b102900d4e5a22a5f061ba846995f61414b68b37cfbec'}
{'block_index': 89, 'transaction_timestamp': '2022-12-11 16:37:36.939804', 'transaction_data': '10/10/2018 14:05, 45', 'proof_of_work': 291, 'previous_hash': '956145a662dd4ba2a658b83ef77effcff7a30086902c086e438a5540eed044c5'}
{'block_index': 90, 'transaction_timestamp': '2022-12-11 16:37:36.958770', 'transaction_data': '26/07/2017 14:23, 393', 'proof_of_work': 6526, 'previous_hash': 'c75b9cb45afe8f3f0909f4ed82469bdc65ba3f32a24ea5a0f7f86613c552ac48'}
{'block_index': 91, 'transaction_timestamp': '2022-12-11 16:37:36.971685', 'transaction_data': '18/04/2020 16:11, 150', 'proof_of_work': 4521, 'previous_hash': 'b0cfa5bc037d4081a6addd4d284f1c916996a8af67dec48c930848b21aacf6fc'}
{'block_index': 92, 'transaction_timestamp': '2022-12-11 16:37:36.975717', 'transaction_data': '20/10/2018 16:46, 50', 'proof_of_work': 1354, 'previous_hash': 'aafe2531d436a3fb1336984b9a4897519402ff3557d5297ad973ee804e88eff3'}
{'block_index': 93, 'transaction_timestamp': '2022-12-11 16:37:36.976707', 'transaction_data': '09/02/2017 09:22, 301', 'proof_of_work': 393, 'previous_hash': '17c44b474e0814704d6a2091244f8fce777d199522cbff3d8dc5a5245897400f'}
{'block_index': 94, 'transaction_timestamp': '2022-12-11 16:37:36.991668', 'transaction_data': '11/06/2020 12:18, 349', 'proof_of_work': 4981, 'previous_hash': '4b6040d96e404b5806d32d7e69dab079fe03f8b34d7539c38d7ef03d55bfdacc'}
{'block_index': 95, 'transaction_timestamp': '2022-12-11 16:37:36.995668', 'transaction_data': '22/08/2020 08:25, 371', 'proof_of_work': 1253, 'previous_hash': '304cd127dfa1bef395a7c859ac465ee9cb50aeecf19841897b2a28fb62e1da64'}
{'block_index': 96, 'transaction_timestamp': '2022-12-11 16:37:36.999648', 'transaction_data': '16/09/2018 08:03, 248', 'proof_of_work': 1359, 'previous_hash': '4ee204e11602f1eb667f18b2dc24db353101a951188648c04b316f07993a8199'}
{'block_index': 97, 'transaction_timestamp': '2022-12-11 16:37:37.006626', 'transaction_data': '28/06/2018 09:00, 236', 'proof_of_work': 2324, 'previous_hash': 'c5de861151dc892fff726f69a2d73b3b746a5c9be95487c07b256000df9f221a'}
{'block_index': 98, 'transaction_timestamp': '2022-12-11 16:37:37.013606', 'transaction_data': '18/10/2019 10:01, 102', 'proof_of_work': 2368, 'previous_hash': '55f2920e8e060e516b1ff6957c3fdd18168bbc8f515a89307b67935d26eba7c3'}
{'block_index': 99, 'transaction_timestamp': '2022-12-11 16:37:37.016598', 'transaction_data': '14/07/2017 13:17, 1', 'proof_of_work': 1163, 'previous_hash': '0f702d3ac641b8e487b0a9a4c253179c7c7347231dcbefc57fcd230773087cae'}
{'block_index': 100, 'transaction_timestamp': '2022-12-11 16:37:37.057734', 'transaction_data': '06/09/2020 06:25, 199', 'proof_of_work': 13762, 'previous_hash': '89e92f884eb6f2bf3db6e8f6426d861f739b5a9d0c9949b696e480178b2cff0e'}
{'block_index': 101, 'transaction_timestamp': '2022-12-11 16:37:37.082448', 'transaction_data': '06/09/2019 11:15, 93', 'proof_of_work': 7222, 'previous_hash': '51772990733388b9080ddb9120732f06bfe8483d52970293443ac231b46cb4b3'}
{'block_index': 102, 'transaction_timestamp': '2022-12-11 16:37:37.082448', 'transaction_data': '10/06/2019 05:31, 70', 'proof_of_work': 179, 'previous_hash': '0e7287e0958531851bd6b30032ac39fd783b99c5adb5914c5f44cd72d270a7a9'}
{'block_index': 103, 'transaction_timestamp': '2022-12-11 16:37:37.090499', 'transaction_data': '28/02/2017 07:47, 302', 'proof_of_work': 2027, 'previous_hash': 'b6ba4831fdd584223ac658bcf2cef033b8c92d8facfa5a73604178c44cddf3bf'}
{'block_index': 104, 'transaction_timestamp': '2022-12-11 16:37:37.093446', 'transaction_data': '25/02/2020 19:21, 326', 'proof_of_work': 631, 'previous_hash': '7487e620189dda5bf86c3d8930e902cb6addfc7167fcdc917b1ba982d0cd1072'}
{'block_index': 105, 'transaction_timestamp': '2022-12-11 16:37:37.113393', 'transaction_data': '12/08/2019 11:48, 85', 'proof_of_work': 5238, 'previous_hash': '9f37e61d398794a09d0bef32ad199e84fba7d2eb8c509f451e319f0da2a3e28c'}
{'block_index': 106, 'transaction_timestamp': '2022-12-11 16:37:37.115387', 'transaction_data': '28/06/2020 12:29, 176', 'proof_of_work': 398, 'previous_hash': 'c79bb5f6a695b51c104204e080e1a5b4c38b56a41cb46064f1c243ab3e496dee'}
{'block_index': 107, 'transaction_timestamp': '2022-12-11 16:37:37.150353', 'transaction_data': '20/06/2018 17:21, 26', 'proof_of_work': 9149, 'previous_hash': '0a00d20c2de746130e288a619920d372a65e5875e92396a27edc37f2c4103751'}
{'block_index': 108, 'transaction_timestamp': '2022-12-11 16:37:37.152289', 'transaction_data': '25/12/2019 11:20, 317', 'proof_of_work': 592, 'previous_hash': '235e3c6f6fc5e700c462df8cd21bf5ee62bb29fdfc048089aaf70eb88279f941'}
{'block_index': 109, 'transaction_timestamp': '2022-12-11 16:37:37.162261', 'transaction_data': '19/06/2018 15:09, 228', 'proof_of_work': 2492, 'previous_hash': '856570cd1435ce1e86ba4bfa37655945ba0ab0cc3232777d284a49f07467f79f'}
{'block_index': 110, 'transaction_timestamp': '2022-12-11 16:37:37.162261', 'transaction_data': '29/10/2016 18:41, 187', 'proof_of_work': 41, 'previous_hash': '5229ede0b2cac77d76349889195503409d5af02a35446c273940ab27024171e0'}
{'block_index': 111, 'transaction_timestamp': '2022-12-11 16:37:37.170252', 'transaction_data': '28/08/2019 06:00, 88', 'proof_of_work': 2326, 'previous_hash': '8826005741eee5cfb5e1594129309ad937357dedb69d0641b1353a86696bb1a0'}
{'block_index': 112, 'transaction_timestamp': '2022-12-11 16:37:37.193178', 'transaction_data': '30/06/2019 07:03, 74', 'proof_of_work': 8163, 'previous_hash': '200df4f7c6f939f6bf4abb28807cd2b96531e5f1d07b756db01e1add3f89190c'}
{'block_index': 113, 'transaction_timestamp': '2022-12-11 16:37:37.193178', 'transaction_data': '28/04/2017 11:39, 79', 'proof_of_work': 168, 'previous_hash': '042be27c89d35855fdfe1d8afff5c13986a1da3578a1963e63b4ef553a51168a'}
{'block_index': 114, 'transaction_timestamp': '2022-12-11 16:37:37.196170', 'transaction_data': '27/12/2019 14:04, 122', 'proof_of_work': 1209, 'previous_hash': '14be4b2be7817764a4e6e34b76d7b16c303a3fd8ba14ba21c8c681f1fb2727d6'}
{'block_index': 115, 'transaction_timestamp': '2022-12-11 16:37:37.218112', 'transaction_data': '15/10/2020 07:57, 385', 'proof_of_work': 7786, 'previous_hash': 'e361e59bcf8f6c725cd6ed8bdd0ae5052716d20820253d1f76ad0cd318f9d284'}
{'block_index': 116, 'transaction_timestamp': '2022-12-11 16:37:37.219110', 'transaction_data': '16/07/2018 08:23, 239', 'proof_of_work': 517, 'previous_hash': '6bd28a1e76e6236908631ee1b31ca01d5ad023929a9b0cfc226e7ea4831cca0f'}
{'block_index': 117, 'transaction_timestamp': '2022-12-11 16:37:37.225093', 'transaction_data': '26/02/2020 09:10, 137', 'proof_of_work': 2243, 'previous_hash': 'a39bbc75eb5f5fc63c5e235d36389b96ba67fa0a5b436600c90a97dd7ba8a6df'}
{'block_index': 118, 'transaction_timestamp': '2022-12-11 16:37:37.259003', 'transaction_data': '16/06/2020 14:51, 171', 'proof_of_work': 12347, 'previous_hash': 'a503bdfe5cf25c61503f6287815c3f8618dca3cb0c312a187272416b09b27a14'}
{'block_index': 119, 'transaction_timestamp': '2022-12-11 16:37:37.261994', 'transaction_data': '18/05/2020 13:46, 345', 'proof_of_work': 814, 'previous_hash': 'b6a9d60ff8682824c5521ff087ad0f5422e25b69ec75aa0f13c3694e62ac364f'}
{'block_index': 120, 'transaction_timestamp': '2022-12-11 16:37:37.276955', 'transaction_data': '02/10/2019 10:18, 294', 'proof_of_work': 5606, 'previous_hash': '795ff902bf2f895624ec303a8511c33ad0b68b4757c6b869773b1abab0eb1e72'}
{'block_index': 121, 'transaction_timestamp': '2022-12-11 16:37:37.283935', 'transaction_data': '25/09/2019 06:13, 292', 'proof_of_work': 2460, 'previous_hash': '9642965a3754cbf633efc555dc0b01218a49090d65fcf6f9e45fdb1f1221fec2'}
--The length of blockchain is  121

Press 'Enter' to exit

Thank you

"""