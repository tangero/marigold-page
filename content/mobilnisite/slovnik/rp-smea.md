---
slug: "rp-smea"
url: "/mobilnisite/slovnik/rp-smea/"
type: "slovnik"
title: "RP-SMEA – RP SME-Address"
date: 2025-01-01
abbr: "RP-SMEA"
fullName: "RP SME-Address"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rp-smea/"
summary: "Adresní pole v rámci přenosového protokolu (RP) používané pro SMS přes IMS. Nese adresu entity krátké zprávy (SME), což je typicky výchozí nebo cílová hodnota MSISDN (telefonní číslo) pro SMS. Je nezb"
---

RP-SMEA je adresní pole v rámci přenosového protokolu (Relay Protocol) používaného pro SMS přes IMS, které nese adresu entity krátké zprávy (Short Message Entity), typicky číslo odesílatele nebo příjemce, a slouží k identifikaci odesílatele nebo příjemce.

## Popis

RP-SMEA, neboli [RP](/mobilnisite/slovnik/rp/) SME-Address, je klíčový parametr v datové struktuře přenosového protokolu (RP) používané pro službu krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)) přes IP multimediální subsystém (IMS). [SME](/mobilnisite/slovnik/sme/) (Short Message Entity) je jakákoli entita, která může iniciovat nebo ukončit krátkou zprávu; nejčastěji jde o uživatelské zařízení (UE) mobilního účastníka, ale může to být také aplikace nebo služba. Pole RP-SMEA obsahuje adresu této entity. V kontextu mobilně-terminovaných SMS (zpráva odeslaná na UE) nese RP-SMEA v RP-DATA zprávě adresu zdrojové SME (odesílatele). U mobilně-iniciovaných SMS nebo v odpovědích jako RP-ACK nese adresu cílové nebo odpovídající SME.

Technický formát RP-SMEA je odvozen od adresních formátů používaných v původních SMS přes okruhově přepínané sítě. Typicky obsahuje typ adresy (např. mezinárodní číslo, národní číslo, alfanumerický řetězec) a samotný řetězec číslic, například [MSISDN](/mobilnisite/slovnik/msisdn/) (např. +1234567890). V rámci RP [PDU](/mobilnisite/slovnik/pdu/) se RP-SMEA nachází spolu s dalšími poli, jako je [RP-MTI](/mobilnisite/slovnik/rp-mti/) a [RP-UI](/mobilnisite/slovnik/rp-ui/). Když IP brána pro krátké zprávy ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) přijme odeslání SMS z UE přes SIP, extrahuje RP-SMEA z RP-DATA, aby identifikovala odesílatele. Naopak, když IP-SM-GW přijme SMS z původního SMSC přes MAP, umístí adresu odesílatele z MAP zprávy do pole RP-SMEA v RP-DATA předtím, než jej vloží do SIP MESSAGE určeného pro příjemce UE.

Jeho role je klíčová pro překlad adres, směrování a prezentaci. UE používá RP-SMEA k zobrazení čísla odesílatele u příchozí zprávy. Dále může být RP-SMEA v síťové logice směrování použito pro aplikaci servisní logiky, jako je filtrování spamu nebo účtování. Hraje také roli při generování doručovacích hlášení; když UE odešle RP-ACK (hlášení o doručení) zpět do sítě, zahrne svou vlastní adresu jako RP-SMEA, což umožní IP-SM-GW korelovat hlášení s původní zprávou a přeposlat jej správnému SMSC a nakonec původnímu odesílateli. Tato transparentnost adresování od konce ke konci je zásadní pro správnou funkci služby SMS v hybridní síti zahrnující prvky IMS i původního okruhově přepínaného jádra sítě.

## K čemu slouží

RP-SMEA bylo definováno, aby se zachovala kritická adresní informace SMS při přechodu z okruhově přepínaného na IMS doručení. V tradičních GSM/UMTS SMS byly adresy odesílatele a příjemce přenášeny v rámci vrstev protokolu MAP. Když se SMS začaly přenášet přes IMS pomocí SIP, existovalo riziko ztráty těchto nezbytných metadat, pokud nebyly explicitně definovány v nové protokolové enkapsulaci. Vrstva RP, včetně pole RP-SMEA, byla vytvořena jako kontejner pro tuto signalizaci specifickou pro SMS, což zajišťuje, že adresní informace zůstaly neporušené a jednoznačné při přenosu uvnitř SIP, který má pro směrování relací vlastní adresní schéma (SIP URI).

Toto vyřešilo základní problém vzájemného propojení: mapování mezi telefonními čísly E.164 (používanými v původním světě SMS) a SIP URI (používanými v IMS). IP-SM-GW funguje jako překladový bod. Používá RP-SMEA z RP zprávy k provádění směrování na základě čísel a identifikaci účastníka, což je nezbytné pro rozhraní s původním domovským registrem polohy (HLR) a SMSC. Bez standardizovaného pole jako je RP-SMEA pro přenos MSISDN by musela IP-SM-GW odvozovat adresu odesílatele/příjemce z jiných, potenciálně méně spolehlivých hlaviček SIP, což by mohlo vést k nesprávnému doručení zpráv, nefunkční prezentaci identifikace volající linky (CLIP) a neúspěšným doručovacím hlášením. RP-SMEA tedy zajišťuje zpětnou kompatibilitu a kontinuitu služby pro jednu z nejrozšířenějších telekomunikačních služeb během vývoje sítě.

## Klíčové vlastnosti

- Nese adresu E.164 (MSISDN) nebo jiný identifikátor entity krátké zprávy (SME).
- Je přítomno v klíčových RP zprávách, jako je RP-DATA a RP-ACK, pro identifikaci původce/příjemce.
- Používá standardizované typy adres a kódování číslic z původních specifikací SMS.
- Nezbytné pro to, aby UE zobrazilo správné informace o odesílateli u příchozí SMS.
- Používá se IP-SM-GW pro rozhodování o směrování a vzájemné propojení s MAP-based SMSC.
- Umožňuje korelaci doručovacích hlášení s původní SMS transakcí.

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS

---

📖 **Anglický originál a plná specifikace:** [RP-SMEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rp-smea/)
