---
slug: "fbs"
url: "/mobilnisite/slovnik/fbs/"
type: "slovnik"
title: "FBS – False Base Station"
date: 2025-01-01
abbr: "FBS"
fullName: "False Base Station"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fbs/"
summary: "Nevlastní nebo škodlivá základnová stanice, která se vydává za legitimní síťovou buňku, aby zachytávala, manipulovala nebo odepírala služby uživatelskému zařízení (UE). Představuje kritické bezpečnost"
---

FBS (Falešná základnová stanice) je škodlivá základnová stanice, která se vydává za legitimní buňku s cílem zachytávat, manipulovat nebo odepírat služby uživatelskému zařízení.

## Popis

False Base Station (FBS) je škodlivý rádiový vysílač, který se maskuje jako legitimní buňka mobilního operátora. Funguje tak, že vysílá synchronizační signály a systémové informace totožné nebo podobné těm od skutečné základnové stanice (např. [eNB](/mobilnisite/slovnik/enb/) nebo gNB), typicky se silnějším signálem, aby přilákala blízká uživatelská zařízení (UE). Jakmile se UE přihlásí nebo připojí k FBS, útočník získá privilegovanou pozici pro zahájení různých útoků. FBS může fungovat jako prostředník (man-in-the-middle), zachycovat uplinkový i downlinkový provoz včetně uživatelských dat, signalizačních zpráv a autentizačních vektorů. Může také odepřít službu tím, že zabrání UE v přístupu ke skutečné síti, nebo snížením bezpečnostního kontextu na slabší, zastaralé algoritmy.

Architektura útoku pomocí FBS zahrnuje nelegitimní stanici, která napodobuje fyzickou vrstvu a protokoly nižších vrstev. Vysílá legitimně vypadající identifikátor veřejné pozemní mobilní sítě (PLMN ID), kód sledovací oblasti a ID buňky. Pokročilé implementace FBS dokážou dokončit počáteční procedury připojení, včetně Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), přeposíláním zpráv mezi UE a skutečnou core sítí, nebo mohou pracovat v samostatném režimu s simulovanou core sítí. To umožňuje získání Mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a dalších citlivých identifikátorů prostřednictvím procedur žádosti o identitu, dokonce i od UE v idle módu.

3GPP řešilo hrozbu FBS napříč několika releasy, primárně v bezpečnostních specifikacích (řada 33). Strategie zmírnění jsou vícevrstvé. Detekce na straně sítě může zahrnovat monitorování anomálií, jako jsou neočekávané konfigurace buněk, nesrovnalosti v síle signálu nebo geografické nemožnosti. Detekce asistovaná UE využívá měření a hlášení podezřelých rádiových podmínek. Dále vylepšení protokolů pro ochranu soukromí a autentizaci, jako je použití Subscription Concealed Identifier (SUCI) namísto IMSI během počáteční registrace, chrání proti pasivním odposlouchávačům IMSI, což je běžná forma FBS. Probíhající vývoj v 5G a dalších generacích se zaměřuje na zlepšení ověřování autenticity základnových stanic sítí a ověřování legitimity sítě ze strany UE.

## K čemu slouží

Koncept False Base Station vychází z inherentní zranitelnosti raných celulárních systémů, kde rádiová signalizace byla z velké části neautentizovaná a uživatelské identity se přenášely v čitelné podobě. Primárním účelem definování a studia FBS v rámci 3GPP je formálně charakterizovat model hrozby, což umožňuje vývoj standardizovaných bezpečnostních protiopatření. Bez takových definic by byla snaha o zmírnění roztříštěná a méně účinná.

Útoky FBS zneužívají základní potřebu UE objevit a připojit se k nejsilnějšímu dostupnému signálu – princip, který zajišťuje kontinuitu služby, ale vytváří bezpečnostní mezeru. Problémy řešené zaměřením na FBS zahrnují prevenci sledování polohy účastníka, odposlechu hovorů a datových relací, podvodů a odepření služby. Historicky byly sítě 2G (GSM) obzvláště zranitelné kvůli slabé vzájemné autentizaci, což z odposlouchávačů [IMSI](/mobilnisite/slovnik/imsi/) učinilo rozšířený nástroj. Motivací práce 3GPP je tyto mezery uzavřít návrhem systémů, kde se síť autentizuje vůči UE a uživatelské soukromí je chráněno od počátečního rádiového kontaktu, čímž se zvyšují náklady a složitost pro útočníky při nasazení úspěšných útoků FBS.

## Klíčové vlastnosti

- Napodobuje legitimní synchronizační signály buňky (PSS/SSS) a vysílací kanály (PBCH)
- Může fungovat jako pasivní odposlouchávač IMSI nebo aktivní prostředník (man-in-the-middle)
- Zneužívá procedury řízení rádiových prostředků (RRC) k zachycení identit účastníků
- Může vynutit snížení úrovně bezpečnostních algoritmů nebo navázat spojení bez šifrování
- Může způsobit odepření služby blokováním přístupu k buňce nebo přesměrováním UE
- Řešeno vylepšeními zabezpečení 3GPP, jako je SUCI a autentizace sítě

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 33.700** — 3GPP TR 33.700
- **TS 33.701** (Rel-19) — Study on mitigations against bidding down attacks

---

📖 **Anglický originál a plná specifikace:** [FBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fbs/)
