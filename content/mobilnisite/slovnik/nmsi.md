---
slug: "nmsi"
url: "/mobilnisite/slovnik/nmsi/"
type: "slovnik"
title: "NMSI – National Mobile Station Identifier"
date: 2025-01-01
abbr: "NMSI"
fullName: "National Mobile Station Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nmsi/"
summary: "Jedinečný identifikátor přidělený mobilní stanici (MS) pro národní použití v rámci sítě konkrétní země. Slouží jako klíč pro identifikaci účastníka a směrování v národním kontextu, odlišný od mezináro"
---

NMSI je jedinečný identifikátor přidělený mobilní stanici pro národní identifikaci účastníka a směrování v rámci sítě konkrétní země.

## Popis

National Mobile Station Identifier (NMSI) je identifikátor účastníka definovaný v raných specifikacích GSM a 3GPP pro použití v geografických hranicích jedné země. Je součástí širšího International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). Strukturně se IMSI skládá ze tříciferného Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), dvou- nebo tříciferného Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) a NMSI. NMSI je tedy část IMSI s proměnnou délkou, která jednoznačně identifikuje účastníka v kontextu konkrétního síťového operátora (identifikovaného MNC) v konkrétní zemi (identifikované MCC).

V provozu je NMSI uloženo na [SIM](/mobilnisite/slovnik/sim/) kartě účastníka a v síťovém Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když se mobilní stanice připojí k síti, typicky předloží své IMSI nebo jeho dočasnou derivaci (jako [TMSI](/mobilnisite/slovnik/tmsi/)) pro autentizaci a identifikaci. Síť používá celé IMSI, ale pro mnoho interních operací směrování a vyhledávání v databázích v rámci národní sítě je NMSI (v kombinaci s MNC) kritickým jedinečným klíčem. Jádrová síť jej používá k načtení profilu účastníka, jeho služebních předplatných a aktuálního stavu z HLR/HSS.

Jeho role je základní pro správu účastníků a mobilitu. Zatímco MCC a MNC poskytují globální směrovací informace k nasměrování signalizace na správnou národní síť a operátora, NMSI přesně určuje záznam jednotlivého účastníka. Toto oddělení umožňuje efektivní hierarchické směrování signalizačních zpráv v globálním ekosystému roamingu a zjednodušuje správu databází účastníků pro operátora. Samotné NMSI je typicky sekvenční nebo administrativně přidělené číslo spravované síťovým operátorem.

## K čemu slouží

NMSI bylo vytvořeno jako součást hierarchického adresního schématu pro mobilní účastníky zavedeného v původních standardech GSM. Jeho účelem je poskytnout národně vymezený jedinečný identifikátor, který v kombinaci s Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) umožňuje jednoznačnou identifikaci účastníka v rámci jedné země. Tento návrh vyřešil problém vytvoření globálně jedinečné identity účastníka (IMSI), přičemž umožnil, aby části této identity byly smysluplné pro národní směrování a správu na úrovni operátora.

Před takovými standardizovanými hierarchickými identifikátory byly schémata adresování účastníků často ad-hoc a nebyla navržena pro globální interoperabilitu vyžadovanou pro mezinárodní roaming. Struktura NMSI/IMSI elegantně odděluje odpovědnosti: MCC/MNC směruje dotazy na správný národní HLR sítě a NMSI je pak tímto HLR použito k nalezení konkrétního účastníka. To usnadňuje efektivní signalizaci v roamových sítích založených na SS7 z éry 2G/3G a zjednodušuje přidělování číselných prostorů, protože každý operátor potřebuje spravovat pouze jedinečnost svých vlastních přidělení NMSI.

Historicky bylo jeho zavedení klíčovým faktorem úspěchu GSM jako globálního standardu, neboť poskytlo nezbytný adresní základ pro škálovatelnou správu účastníků a mezinárodní roaming. Zatímco moderní sítě stále více používají na rozhraní vzduchu více ochraňující soukromí dočasné identifikátory, NMSI uvnitř IMSI zůstává trvalým, kořenovým klíčem pro identitu účastníka v databázích jádrové sítě.

## Klíčové vlastnosti

- Součást International Mobile Subscriber Identity (IMSI)
- Jednoznačně identifikuje účastníka u konkrétního síťového operátora v zemi
- Uloženo na SIM kartě a v HLR/HSS
- Používáno jako klíč pro načítání dat účastníka v jádrové síti
- Umožňuje hierarchické směrování pro globální adresování účastníků
- Spravováno a přidělováno jednotlivým síťovým operátorem

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements

---

📖 **Anglický originál a plná specifikace:** [NMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmsi/)
