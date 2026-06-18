---
slug: "twa"
url: "/mobilnisite/slovnik/twa/"
type: "slovnik"
title: "TWA – Two Way Alternate"
date: 2025-01-01
abbr: "TWA"
fullName: "Two Way Alternate"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/twa/"
summary: "TWA je komunikační režim definovaný 3GPP pro protokoly vrstvy spojení datového přenosu, umožňující obousměrnou výměnu dat, kdy se zařízení střídají ve vysílání. Zajišťuje uspořádanou komunikaci preven"
---

TWA je komunikační režim 3GPP na vrstvě spojení datového přenosu pro obousměrnou výměnu, kdy zařízení se střídají ve vysílání, aby se zabránilo kolizím a řídila se přenosová práva na rozhraních jako X2 a S1.

## Popis

Two Way Alternate (TWA) je režim datové komunikace specifikovaný v 3GPP TS 37.462, fungující na vrstvě spojení datového přenosu za účelem usnadnění obousměrné výměny dat mezi dvěma entitami v poloduplexním režimu. V TWA se zařízení komunikují tak, že se střídají ve vysílání dat, přičemž jedno zařízení funguje jako primární vysílač, zatímco druhé čeká, a role se podle potřeby střídají. Tento režim je běžně implementován v protokolech jako [LAPD](/mobilnisite/slovnik/lapd/) (Link Access Procedure on the D-channel) nebo [HDLC](/mobilnisite/slovnik/hdlc/) (High-Level Data Link Control), používaných na rozhraních jako [X2](/mobilnisite/slovnik/x2/) (mezi základnovými stanicemi) a S1 (mezi základnovými stanicemi a jádrem sítě). TWA zajišťuje uspořádanou komunikaci vynucováním přísné disciplíny střídání, čímž zabraňuje kolizím dat a efektivně spravuje přenosová práva.

Z architektonického hlediska zahrnuje TWA dvě partnerské entity propojené přes fyzický nebo logický spoj, z nichž každá disponuje vysílací a přijímací vyrovnávací pamětí a je řízena stavovým automatem, který řídí přenosová oprávnění. Mezi klíčové komponenty patří mechanismus poll/final bitu, kdy jedno zařízení dotazuje (poll) druhé, aby mu udělilo přenosová práva, a rámce potvrzení, které potvrzují úspěšný příjem dat. Protokol funguje v vyvážené nebo nevyvážené konfiguraci v závislosti na tom, zda mají obě zařízení stejnou míru kontroly. V sítích 3GPP se TWA často používá na přenosových spojích pro signalizační zprávy, jako jsou příkazy k předání spojení nebo informace o zatížení, kde je spolehlivé a seřazené doručení kritické.

Při provozu TWA funguje tak, že naváže vztah typu master-slave nebo vyvážený dialog mezi rovnocennými partnery. Například při nastavení rozhraní X2 může jedna eNodeB zahájit přenos odesláním rámce s nastaveným poll bitem, což signalizuje, že uvolňuje kanál druhé eNodeB. Příjemce odpoví datovými rámci a nastaví final bit, aby signalizoval dokončení, načež se role obrátí. Toto střídání pokračuje za použití mechanismů řízení toku, jako je okénkování, pro správu datových toků. TWA zvyšuje spolehlivost zahrnutím detekce chyb prostřednictvím kontrolních součtů cyklickou redundancí a opakovaným vysíláním ztracených rámců. Jeho role v sítích 3GPP spočívá v poskytování robustní metody s nízkou režií pro komunikaci řídicí roviny, která zajišťuje doručení kritických signalizačních informací bez rušení, a to i v přetížených scénářích.

## K čemu slouží

TWA byl vyvinut pro řešení potřeby efektivní a bezkolizní obousměrné komunikace v telekomunikačních sítích, zejména pro signalizační spoje, kde jsou objemy dat mírné, ale spolehlivost je prvořadá. Před jeho přijetím mohly jednoduché plně duplexní nebo soutěživé protokoly vést ke kolizím dat nebo složitým požadavkům na vyrovnávací paměť ve sdíleném médiu. TWA poskytuje strukturovaný přístup, který maximalizuje využití spoje při minimalizaci latence a chyb, což jej činí vhodným pro rozhraní jako [X2](/mobilnisite/slovnik/x2/) a S1 v sítích LTE a 5G.

Motivace pro TWA vychází z vývoje architektur mobilních sítí, které vyžadují bezproblémovou koordinaci mezi síťovými prvky pro funkce jako předání spojení a vyrovnávání zátěže. Tím, že umožňuje uspořádané střídání, TWA zajišťuje předvídatelné vysílání signalizačních zpráv, snižuje riziko ztráty paketů a zlepšuje stabilitu sítě. Řeší také omezení dřívějších poloduplexních režimů začleněním pokročilého řízení toku a obnovy po chybách, čímž se přizpůsobuje požadavkům 3GPP na vysokou dostupnost a nízkou latenci. TWA podporuje škálovatelnost tím, že umožňuje více logických kanálů přes jeden fyzický spoj, a optimalizuje tak využití zdrojů v přenosových sítích.

## Klíčové vlastnosti

- Umožňuje poloduplexní obousměrnou komunikaci se střídáním stran
- Zabraňuje kolizím dat prostřednictvím řízeného střídání přenosu
- Používá poll/final bity pro správu oprávnění a řízení toku
- Podporuje detekci chyb a opakování přenosu pro spolehlivost
- Integruje se s protokoly vrstvy spojení datového přenosu, jako jsou LAPD a HDLC
- Umožňuje signalizaci na rozhraních X2 a S1 pro LTE/5G

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)
- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [TWA na 3GPP Explorer](https://3gpp-explorer.com/glossary/twa/)
