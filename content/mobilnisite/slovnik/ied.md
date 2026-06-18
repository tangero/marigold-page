---
slug: "ied"
url: "/mobilnisite/slovnik/ied/"
type: "slovnik"
title: "IED – Information Element Data"
date: 2025-01-01
abbr: "IED"
fullName: "Information Element Data"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ied/"
summary: "Označuje samotnou hodnotu nebo obsahovou část Informačního prvku (IE) v rámci protokolové zprávy 3GPP. Zatímco IE definuje strukturu a význam, IED je konkrétní instance dat přenášených v této struktuř"
---

IED je konkrétní datová hodnota nebo obsah přenášený ve strukturovaném poli Informačního prvku (Information Element) v protokolové zprávě 3GPP, která slouží jako dynamická užitečná část zprávy pro konfiguraci sítě, signalizaci a řízení.

## Popis

Data informačního prvku (IED) jsou skutečný obsah přenášený v poli 'Value' Informačního prvku ([IE](/mobilnisite/slovnik/ie/)). IE je definováno svým Typem (nebo Identifikátorem), Délkou a Hodnotou. IED tvoří právě tuto Hodnotu. Jde o proměnlivá, na konkrétní instanci závislá data, která dávají IE jeho operační význam v dané protokolové transakci. Například IE může být definováno jako 'Identita buňky' s ID typu 0xXX a délkou 2 oktetů. IED pro toto IE v konkrétní [RRC](/mobilnisite/slovnik/rrc/) zprávě by pak byl skutečný dvouoktetový binární číselný identifikátor buňky, například 0x01A3.

Formát a povolený rozsah IED jsou striktně definovány specifikací příslušného IE. IED může být jednoduchý primitivní typ (např. INTEGER, BIT STRING, OCTET STRING, ENUMERATED hodnota) nebo komplexní vnořená struktura (SEQUENCE nebo SEQUENCE OF dalších IE). Pokud jde o SEQUENCE, samotné IED obsahuje zřetězení dalších IED, z nichž každé patří k podřízenému IE. Kódování IED se řídí pravidly specifikovanými pro dané IE, typicky ASN.1 Packed Encoding Rules ([PER](/mobilnisite/slovnik/per/)), které vytvářejí kompaktní, jednoznačný bitový proud. Přijímající entita tento bitový proud dekóduje na základě znalosti definice IE, aby IED správně extrahovala a interpretovala.

IED je mechanismus, prostřednictvím kterého je dosahováno veškerého dynamického řízení sítě. Když síť odešle zprávu RRC Connection Reconfiguration k UE, IED uvnitř obsažených IE specifikují přesně nové radiové přenosové kanály k založení, jejich parametry QoS, konfigurace fyzických kanálů a případná měřicí okna. V [NAS](/mobilnisite/slovnik/nas/) Attach Request přenášejí IED dočasnou identitu UE, bezpečnostní schopnosti a požadovaný síťový řez. Síť tato IED zpracovává, aby rozhodovala o přidělování zdrojů, správě mobility a zřizování relací. Zatímco tedy definice IE poskytuje šablonu, IED poskytuje živá, operační data, která řídí chování sítě na úrovni jednotlivých UE a relací.

## K čemu slouží

Koncept IED existuje, aby oddělil statickou definici informace ([IE](/mobilnisite/slovnik/ie/)) od její dynamické instance (data). Toto oddělení je základním principem návrhu softwaru a protokolů, který zvyšuje flexibilitu, udržovatelnost a efektivitu. Definice IE jsou statické, standardizované a pevně zabudované do specifikací protokolů a softwaru zařízení. IED jsou však generována za běhu na základě aktuálního stavu sítě, uživatelského předplatného, požadované služby a rádiových podmínek.

Tím se řeší problém potřeby nekonečného množství předdefinovaných, pevně zakódovaných zpráv. Uvažujme parametr QoS. IE definuje, že 'QoS Profile' je SEQUENCE obsahující parametry jako [QCI](/mobilnisite/slovnik/qci/), [ARP](/mobilnisite/slovnik/arp/), [GBR](/mobilnisite/slovnik/gbr/) a MBR. IED pro relaci streamování videa může nastavit QCI=2 (GBR video), GBR=5 Mbps, zatímco pro synchronizaci e-mailů na pozadí může IED nastavit QCI=9 (non-GBR). Stejná struktura IE podporuje oba případy a nespočet dalších kombinací čistě prostřednictvím variace v IED. To činí protokol nesmírně výkonným a přizpůsobivým.

Dále to umožňuje efektivní zpracování. Síťové uzly mohou být implementovány s parsery, které rozumějí struktuře IE. Když zpráva dorazí, parser prochází známou strukturou, aby lokalizoval a extrahoval hodnoty IED, které jsou následně předány příslušným logickým modulům (např. scheduleru, správci mobility, policy engine). Bez tohoto strukturovaného oddělení by protokolové zprávy byly neprůhledná data vyžadující komplexní a náchylné k chybám parsování pro každý nový typ zprávy nebo variantu od výrobce. IED uvnitř své definované IE obálky poskytuje čisté, strojově čitelné rozhraní pro síťovou signalizaci.

## Klíčové vlastnosti

- Tvoří proměnné pole 'Value' v rámci TLV struktury Informačního prvku.
- Formát a platné rozsahy jsou striktně omezeny definicí nadřazeného IE.
- Může být jednoduchým datovým typem (celé číslo, řetězec) nebo komplexní vnořenou strukturou dalších IED.
- Je kódováno podle pravidel protokolu (např. ASN.1 PER) pro efektivní přenos.
- Představuje na konkrétní instanci závislá, operační data, která řídí chování sítě.
- Je přijímací stranou parsováno a interpretováno na základě znalosti přidruženého IE.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [IED na 3GPP Explorer](https://3gpp-explorer.com/glossary/ied/)
