�
    ��!d�  �                   �  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ 	 d dl	Z
d dlmZ n'#   ej        d�  �          ej        d�  �         Y nxY wd� Zd� Zd� Zd	Zg Zd ad a e�   �           ed
�  �        Z	  eed�  �        �                    �   �          n	#  dZY nxY wd� Zd� Zd� Zg d�Zd� Zd� Zd� Z 	  e�   �         \  Z!Z"Z# e$e!�  �        dk    r ee!e"�  �         n ee!e#e"�  �          e �   �           e%dez   �  �          ed�  �        Z&e&dv r+ e�   �         \  Z!Z"Z#d ad ag Z ee!e"�  �          e �   �          ndS ��)�    N)�ThreadPoolExecutor)�BeautifulSoupzpip install bs4 requests�clearc                  �V   � t          j        d�  �         t          t          �  �         d S )Nr   )�os�system�print�sa� �    �
newdump.pyr   r   
   s!   � ���7�����r�����r   c                  �.   � t          t          �  �         d S �N)r	   r
   r   r   r   �logor      s   � ��r�����r   c                  �$   � t          d�  �         d S )Nz5[1;37m----------------------------------------------)r	   r   r   r   �linexr      s   � ��@�A�A�A�A�Ar   u�   
[1;37m----------------------------------------------
→   CODED BY      :  Cyber Demon 
 
[1;37m----------------------------------------------zSave file to : �rz/sdcard/RDUMP.txtc                 ��   � dt          | �  �        z
  }t          d|z  �  �        dz   }t          |�  �        D ]?}t          �                    | t          |�  �        �                    |�  �        z   �  �         �@d S )N�   �9�   )�len�int�range�uids�append�str�zfill)�code�ln�lim�is       r   �sr#   "   so   � �	�#�d�)�)�|�B��C��H���a��C��3�Z�Z� +� +�����D��Q�����b�)�)�)�*�*�*�*�+� +r   c                 �  � t          �   �          t          d�  �         t          �   �          t          t	          d�  �        �  �        }t          �   �          t          d�  �         t          d�  �         t          �   �          |dk    rt          | �  �         d S t          |�  �        D ]Y}t          �                    | d�	                    d� t          dt          | �  �        z
  �  �        D �   �         �  �        z   �  �         �Zd S )	Nz[1] Select 1 for counting ..z
select :  z process his been started ...z Use CTRL+z for stop�   � c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S r   ��random�choice�string�digits��.0�_s     r   �	<genexpr>zgen.<locals>.<genexpr>5   s>   � � � � %� %�a�V�]�6�=�%A�%A� %� %� %� %� %� %r   r   )r   r	   r   r   �inputr#   r   r   r   �joinr   )r   �tt�opr"   s       r   �genr5   (   s  � �	�G�G�G�	�
(�)�)�)�	�G�G�G�
�5�!�"�"�#�#�B�	�G�G�G�	�
)�*�*�*�	�
 �!�!�!�	�G�G�G�	�1�u�u�	�$�������r��� 	� 	�A��K�K��R�W�W� %� %�5�
�3�t�9�9��L
� L
� %� %� %� � � � � � � �	� 	r   c                 ��   � t          |�  �        D ]Y}t          �                    | d�                    d� t          |t	          | �  �        z
  �  �        D �   �         �  �        z   �  �         �Zd S )Nr&   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S r   r(   r-   s     r   r0   zgeno.<locals>.<genexpr>;   s>   � � � � !� !�!���v�}�!=�!=� !� !� !� !� !� !r   )r   r   r   r2   r   )r   �lr3   r"   s       r   �genor9   9   s�   � ��2�Y�Y� � �����D���� !� !�u�	�#�d�)�)��H
� H
� !� !� !� � � � 	� 	� 	� 	�� r   )zcMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101z�Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1z@Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)z=Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)z;Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)c                  �  � t          j        d�  �         t          t          �  �         t          d�  �         t	          �   �          t          d�  �        } t          �   �          t          d�  �         t	          �   �          t          t          d�  �        �  �        }d}t          | �  �        dk     rt          t          d�  �        �  �        }| ||fS )	Nr   z$ Example : 10001 ,100089,100090**etczSelect your link : z*Example : 10000,100000,300000,3000484, etczTotal ids :r   �   zUid length: )	r   r   r	   r
   r   r1   r   r   r   )r   r3   r8   s      r   �inputsr<   D   s�   � ��I�g����	�"�I�I�I�	�
0�1�1�1�	�G�G�G�	�$�	%�	%�D�	�G�G�G�	�
6�7�7�7�	�G�G�G�
�5���� � �B��A�
�4�y�y��{�{�
�e�N�#�#�
$�
$����1�9�r   c                 �b  � t          j        t          �  �        }dd|d�}d| z   }t          j        ||��  �        }t          |j        d�  �        }|�                    d�  �        j        �	                    d�  �        d	         �
                    �   �         }d
|vrsd|vrot          dz  at          d| � dt          � ��  �         t          t          d�  �        �                    | dz   |z   dz   �  �         t          d| � dt          � ��  �         t          dz  at          dt          z  d��  �         d S )Nzm.facebook.com�GET)�	authority�methodz
user-agentz&https://m.facebook.com/profile.php?id=)�headerszhtml.parser�title�|r   zContent not foundzLog in to Facebookr   z[1;32mz | �a�
z[1;34mz[Couting : %s ]�)�end)r)   r*   �uaor   �get�bs�content�find�text�split�strip�nr	   �c�open�file�write)�uid�ua�hd�url�pi�bp�names          r   �getnamer\   V   s:  � ��}�S���B�$���� �B� 	1��4�C��u�S�����B�	�"�*�]�#�#�B�	����	�	�	�	$�	$�S�	)�	)�!�	,�	2�	2�	4�	4�D��$�&�&�+?�t�+K�+K�	�1��� 	�&�3�&�&�1�&�&�'�'�'��T�#�����S��Y�t�^�D�0�1�1�1��&�3�&�&�1�&�&�'�'�'��q�D�A�	�
�a�
 �T�*�*�*�*�*�*r   c                  �   � t          d��  �        5 } t          D ]}| �                    t          |�  �         �	 d d d �  �         d S # 1 swxY w Y   d S )N�   )�max_workers)�tdpr   �submitr\   )�trU   s     r   �runrc   s   s�   � �	��	�	�	� "��� 	"� 	"�C��H�H�W�S�!�!�!�!�	"�"� "� "� "� "� "� "� "� "� "� "� "���� "� "� "� "� "� "s   �&A�A	�A	Tr;   zDumped ids are saved in: zDump again? [Y or N])�Y�y)'r)   r+   �time�re�sysr   �concurrent.futuresr   r`   �requestsr   �bs4r   rJ   r   r   r   r   r
   r   rP   rQ   r1   rS   rR   �readr#   r5   r9   rH   r<   r\   rc   r   r3   r8   r   r	   �rrr   r   r   �<module>rn      s�  �� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� #� 8� 8� 8� 8� 8� 8������'�'�'�'�'�'�'����B�I�(�)�)�)��B�I�g���������� � �� � �B� B� B�;��
 ������ �����
�U�������D��c�N�N���������	�D�D�D����+� +� +�� � �"� � �?� ?� ?��� � �$+� +� +�:"� "� "���f�h�h�I�D��A�
�s�4�y�y�!�|�|���D��������T�!�B�����C�E�E�E�	�E�
%�d�
*�+�+�+��u�#�$�$�B�	�Y����&�(�(�	��R��
��
������D�������������%s   �
+ �"A�9B �B