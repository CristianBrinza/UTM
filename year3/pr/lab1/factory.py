from LAB2 import player_pb2
from player import Player
import xml.etree.ElementTree as ET



class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        json_list = []
        for player in players:
            player_dict = {
                "nickname": player.nickname,
                "email": player.email,
                "date_of_birth": player.date_of_birth.strftime("%Y-%m-%d"),
                "xp": player.xp,
                "class": player.cls
            }
            json_list.append(player_dict)

        return json_list
        pass

    def from_json(self, list_of_dict):
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        players = []

        for data in list_of_dict:
            player = Player(
                data['nickname'],
                data['email'],
                data['date_of_birth'],
                data['xp'],
                data['class']
            )
            players.append(player)

        return players

        pass

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        root = ET.fromstring(xml_string)
        players = []

        for player_element in root.findall('player'):
            nickname = player_element.find('nickname').text
            email = player_element.find('email').text
            date_of_birth = player_element.find('date_of_birth').text
            xp = int(player_element.find('xp').text)
            cls = player_element.find('class').text
            players.append(Player(nickname, email, date_of_birth, xp, cls))

        return players
        pass

    def to_xml(self, players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        data = ET.Element("data")

        for player in players:
            player_element = ET.SubElement(data, 'player')

            ET.SubElement(player_element, 'nickname').text = player.nickname
            ET.SubElement(player_element, 'email').text = player.email
            ET.SubElement(player_element, 'date_of_birth').text = player.date_of_birth
            ET.SubElement(player_element, 'xp').text = str(player.xp)
            ET.SubElement(player_element, 'class').text = player.player_class

        return ET.tostring(data).decode()

        pass

    def from_protobuf(self, binary):
        players_list = player_pb2.PlayersList()
        players_list.ParseFromString(binary)

        players = []

        aa={
           0: 'Berserk',
        1:'Tank',
        3:'Paladin',
        4:'Mage'
        }
        for p in players_list.player:
            player = Player(
                p.nickname,
                p.email,
                p.date_of_birth,
                p.xp,
                aa[p.cls]
            )

            players.append(player)
        return players

        pass

    def to_protobuf(self, list_of_players):
        '''
            This function should transform a list with Player objects intoa binary protobuf string.
        '''
        players_list = player_pb2.PlayersList()

        for player in list_of_players:
            p = players_list.player.add()
            p.nickname = player.nickname
            p.email = player.email
            p.date_of_birth = player.date_of_birth.strftime("%Y-%m-%d")
            p.xp = player.xp
            p.cls = player_pb2.Class.Value(player.cls)

        return players_list.SerializeToString()

        pass

