---
slug: "smr"
url: "/mobilnisite/slovnik/smr/"
type: "slovnik"
title: "SMR – Short Message Relay"
date: 2022-01-01
abbr: "SMR"
fullName: "Short Message Relay"
category: "Services"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/smr/"
summary: "Short Message Relay (SMR) je síťová entita zavedená pro testování služby krátkých zpráv mezi UE. Funguje jako prostředník, který přijme SMS od testovacího UE, upraví konkrétní prvky protokolu podle po"
---

SMR je síťová entita pro testování SMS, která funguje jako prostředník: přijme zprávu od testovacího UE, podle pokynů upraví konkrétní prvky protokolu a přepošle ji cílovému UE.

## Popis

Short Message Relay (SMR) je specializovaná síťová entita definovaná v testovacích specifikacích 3GPP pro shodu, konkrétně pro testování chování uživatelského zařízení (UE) ve vztahu ke službě krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)). Nejde o standardní provozní síťový prvek v komerčních sítích, nýbrž o klíčovou součást architektury testovacího systému. Primární funkcí SMR je usnadnění testování SMS mezi UE tím, že funguje jako řízený prostředník. V typickém testovacím scénáři testovací UE (odesílatel) odešle SMS. Místo směrování přes komerční [SMSC](/mobilnisite/slovnik/smsc/) je zpráva zachycena SMR. SMR, která je pod kontrolou testovacího systému, může následně programově změnit konkrétní pole v rámci datových jednotek SMS protokolu před přeposláním (relaying) zprávy cílovému UE (příjemci).

Provozně SMR komunikuje s testovacím UE přes rádiovou přístupovou síť (např. [E-UTRAN](/mobilnisite/slovnik/e-utran/) pro LTE testy dle 36.509) a signalizační cesty jádrové sítě používané pro SMS, jako jsou cesty přes [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum). Testovací systém nakonfiguruje SMR konkrétními instrukcemi pro daný testovací případ. Tyto instrukce určují, které parametry se mají upravit. Například SMR může změnit TP-Protocol-Identifier (TP-PID), TP-Data-Coding-Scheme (TP-DCS) nebo záměrně zavést chybu v délce TP-User-Data. Může také manipulovat s TP-Destination-Address nebo TP-Originating-Address, aby simulovala různé síťové scénáře. Po provedení úprav SMR přepošle zprávu směrem k cílovému UE. Chování jak odesílajícího UE (např. jeho reakce na hlášení o selhání), tak přijímajícího UE (např. jeho schopnost správně dekódovat upravenou zprávu) je následně pozorováno a ověřováno vůči specifikacím 3GPP.

Architektura SMR je navržena pro přesnost a opakovatelnost testování. Umožňuje testovacím inženýrům vytvářet složité, hraniční scénáře, které by bylo obtížné nebo nemožné vytvořit pomocí standardních síťových prvků. Tím, že oddělí testovací podnět (upravenou SMS) od běžného chování komerčního SMSC, poskytuje SMR čisté, instrumentované prostředí pro ověřování implementace protokolového zásobníku UE. Její role je klíčová pro zajištění, aby UE od různých výrobců interpretovala parametry SMS konzistentně a robustně zvládala chybové stavy, čímž se zaručuje interoperabilita a spolehlivost služby v živých sítích. Specifikace 36.509 podrobně popisuje přesné požadavky a očekávané chování SMR pro testování shody LTE UE.

## K čemu slouží

Short Message Relay (SMR) byla vytvořena, aby vyplnila konkrétní mezeru v metodologii testování shody UE: potřebu řízeného, deterministického a flexibilního mechanismu pro testování end-to-end [SMS](/mobilnisite/slovnik/sms/) procedur mezi dvěma UE. Tradiční testování SMS často spoléhalo na komerční [SMSC](/mobilnisite/slovnik/smsc/) nebo jednoduchý testovací SMSC, kterým chyběla detailní kontrola potřebná k manipulaci s jednotlivými poli protokolu pro každou zprávu zvlášť. To ztěžovalo testování, jak UE zareaguje na nestandardní, chybné nebo specifické kombinace parametrů SMS – podmínky, které jsou pro ověření robustní implementace a interoperability zásadní.

Jak se SMS vyvíjela s novými funkcemi a kódovacími schématy (jako [UCS-2](/mobilnisite/slovnik/ucs-2/) pro Unicode, třídní zasílání zpráv nebo žádosti o stavové hlášení), rostla i složitost protokolu. Zajištění, aby každé UE správně generovalo, parsovalo a reagovalo na všechny platné i neplatné formáty zpráv, se stalo kritickým úkolem zajištění kvality pro výrobce a certifikační orgány. SMR poskytuje v rámci testovacího systému specializovaný nástroj pro generování těchto přesných testovacích podmínek. Řeší problém reprodukovatelnosti testů tím, že umožňuje opakovaně přeposílat přesně stejnou upravenou zprávu, což je klíčové pro ladění a certifikaci.

Navíc SMR podporuje testování v izolovaných laboratorních prostředích bez nutnosti připojení k živému operátorskému SMSC. To je nezbytné pro předcertifikační testování prováděné výrobci UE. Tím, že simuluje roli sítě v přenosové cestě SMS, umožňuje SMR komplexní testování implementace SMS vrstvy v UE vůči specifikacím 3GPP TS 24.011 a souvisejícím dokumentům. Její zavedení standardizovalo dříve často ad-hoc, výrobci specifická testovací nastavení, což vedlo k důslednějším a spolehlivějším výsledkům testování UE napříč odvětvím.

## Klíčové vlastnosti

- Funguje jako programovatelný prostředník pro SMS mezi UE v testovacích systémech pro shodu
- Umí upravovat konkrétní parametry SMS na vrstvě TP (Transfer Protocol) (např. TP-PID, TP-DCS, adresy) pod kontrolou testu
- Podporuje vytváření testovacích případů pro normální i abnormální SMS procedury
- Umožňuje testování chování UE v reakci na manipulovaný nebo chybný obsah zprávy
- Poskytuje deterministické a opakovatelné testovací prostředí izolované od komerčních SMSC
- Podrobné požadavky a chování specifikovány v testovacích specifikacích 3GPP (např. 36.509 pro LTE)

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)

## Definující specifikace

- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions

---

📖 **Anglický originál a plná specifikace:** [SMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/smr/)
