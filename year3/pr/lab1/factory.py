import xml.etree.ElementTree as ET
import player_pb2

from player import Player


class PlayerFactory:
    def to_json(self, players):

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
        players_temp = []

        for data in list_of_dict:
            player = Player(
                data["nickname"],
                data["email"],
                data["date_of_birth"],
                data["xp"],
                data["class"]
            )
            players_temp.append(player)

        return players_temp

        pass

    def from_xml(self, xml_string):
        root = ET.fromstring(xml_string)
        players = []

        for player_elem in root.findall('player'):
            nickname = player_elem.find('nickname').text
            email = player_elem.find('email').text
            date_of_birth = player_elem.find('date_of_birth').text
            xp = int(player_elem.find('xp').text)
            cls = player_elem.find('class').text
            players.append(Player(nickname, email, date_of_birth, xp, cls))

        return players
        pass
    def to_xml(self, list_of_players):
        data = ET.Element('data')

        for player in list_of_players:
            player_elem = ET.SubElement(data, 'player')
            ET.SubElement(player_elem, 'nickname').text = player.nickname
            ET.SubElement(player_elem, 'email').text = player.email
            ET.SubElement(player_elem, 'date_of_birth').text = player.date_of_birth.strftime('%Y-%m-%d')
            ET.SubElement(player_elem, 'xp').text = str(player.xp)
            ET.SubElement(player_elem, 'class').text = player.cls

        return ET.tostring(data, encoding='utf-8').decode('utf-8')
    pass

    # TODO
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