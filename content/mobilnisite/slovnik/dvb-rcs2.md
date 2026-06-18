---
slug: "dvb-rcs2"
url: "/mobilnisite/slovnik/dvb-rcs2/"
type: "slovnik"
title: "DVB-RCS2 – Second Generation Digital Video Broadcasting - Return Channel via Satellite"
date: 2025-01-01
abbr: "DVB-RCS2"
fullName: "Second Generation Digital Video Broadcasting - Return Channel via Satellite"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dvb-rcs2/"
summary: "Standard DVB druhé generace pro interaktivní satelitní systémy, který specifikuje zpětný kanál od uživatelských terminálů k satelitní síti. Poskytuje vyšší efektivitu využití šířky pásma, podporu služ"
---

DVB-RCS2 je standard druhé generace DVB pro interaktivní satelitní zpětný kanál, který poskytuje vyšší efektivitu, podporu IP a QoS pro širokopásmové komunikace a je integrován v 3GPP pro satelitní přenos (backhaul) a NTN.

## Popis

DVB-RCS2 (Second Generation Digital Video Broadcasting - Return Channel via Satellite) je standard [DVB](/mobilnisite/slovnik/dvb/), který definuje rozhraní vzdušného rozhraní a protokoly pro zpětný kanál (od uživatelského terminálu k síti) v interaktivních satelitních systémech. V rámci 3GPP je odkazován pro integraci sítě neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)), zejména pro satelitní přenos (backhaul) a uživatelská zařízení se satelitní zpětnou schopností. Architektura se skládá z terminálu zpětného satelitního kanálu ([RCST](/mobilnisite/slovnik/rcst/)) na straně uživatele, satelitu s transparentní nebo regenerační užitečnou zátěží a brány nebo síťového řídicího centra ([NCC](/mobilnisite/slovnik/ncc/)), které spravuje přidělování prostředků a řízení spojení.

Protokol pracuje pomocí schématu vícefrekvenčního časového multiplexu s děleným přístupem (MF-TDMA) pro zpětný kanál, kde NCC dynamicky přiděluje časové sloty a nosné frekvence RCSTům na základě poptávky. Podporuje adaptivní kódování a modulaci ([ACM](/mobilnisite/slovnik/acm/)) pro optimalizaci výkonu spoje za různých povětrnostních podmínek. Klíčové součásti zahrnují protokoly nižší vrstvy (fyzická a spojová vrstva) pro robustní přenos přes satelit a vyšší vrstvu, která je plně založena na IP, což umožňuje bezproblémovou integraci s pozemními IP sítěmi. NCC používá plán časování terminálových burstů (TBTP) pro komunikaci přidělení prostředků k terminálům.

Jeho úlohou v sítích 3GPP je poskytnout standardizovanou, efektivní zpětnou cestu pro satelitní komunikaci, což umožňuje interaktivní služby jako širokopásmový internet, VoIP a podnikové [VPN](/mobilnisite/slovnik/vpn/) přes satelit. Pro 5G NTN může DVB-RCS2 sloužit jako protokol zpětného kanálu pro uživatelská zařízení nebo jako součást satelitního přenosu (backhaul) pro základnové stanice, čímž zajišťuje interoperabilitu mezi satelitními a pozemními segmenty. Podporuje rozlišení kvality služeb (QoS), což je nezbytné pro integraci s rámcem QoS 3GPP.

## K čemu slouží

DVB-RCS2 byl vyvinut k překonání omezení standardu první generace DVB-RCS, který měl nižší spektrální účinnost a omezenou podporu moderních IP služeb. Řeší rostoucí poptávku po vysokorychlostním, interaktivním širokopásmovém připojení přes satelit, zejména ve vzdálených a mobilních scénářích, kde není dostupná pozemní infrastruktura. Motivací bylo vytvořit flexibilnější, efektivnější a na IP zaměřený standard pro snížení nákladů na přenesený bit a podporu širšího spektra aplikací.

V kontextu 3GPP je DVB-RCS2 integrován, aby poskytoval standardizované řešení zpětného kanálu pro satelitní komponenty v 5G neterestrických sítích. Tím se řeší problém proprietárních satelitních zpětných kanálů a umožňuje se interoperabilita mezi satelitními operátory a operátory mobilních sítí. Umožňuje systémům 3GPP rozšířit pokrytí do nedostatečně pokrytých oblastí pomocí satelitů, podporujících jak spotřebitelské širokopásmové připojení, tak přenos (backhaul) pro kritické IoT aplikace se zaručenou QoS.

## Klíčové vlastnosti

- MF-TDMA s dynamickým přidělováním kapacity
- Plně IP protokolový zásobník (podpora IPv4/IPv6)
- Adaptivní kódování a modulace (ACM) pro optimalizaci spoje
- Komplexní podpora QoS s třídami provozu
- Vylepšená bezpečnost s volitelným šifrováním na spojové vrstvě
- Podpora mobilních terminálů (leteckých, námořních, pozemních mobilních)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [DVB-RCS2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvb-rcs2/)
