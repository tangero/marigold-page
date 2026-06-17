---
slug: "aea"
url: "/mobilnisite/slovnik/aea/"
type: "slovnik"
title: "AEA – Advanced Emergency Alert"
date: 2025-01-01
abbr: "AEA"
fullName: "Advanced Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aea/"
summary: "AEA je systém standardizovaný organizací 3GPP pro doručování kritických veřejných varování na mobilní zařízení během mimořádných událostí. Umožňuje orgánům vysílat geograficky cílená varování s multim"
---

AEA je systém standardizovaný organizací 3GPP pro doručování geograficky cílených multimediálních veřejných varování na mobilní zařízení během mimořádných událostí za účelem zajištění rychlého a spolehlivého šíření životně důležitých informací.

## Popis

Advanced Emergency Alert (AEA) je komplexní systém veřejného varování standardizovaný ve 3GPP Release 15 a následujících verzích, navržený pro doručování kritických informací o mimořádných událostech mobilním uživatelům prostřednictvím buněčných sítí. Systém funguje jako nadstavbová služba využívající stávající infrastrukturu 4G LTE a 5G NR a k zajištění spolehlivého doručení zprávy využívá vyhrazené vysílací mechanismy, a to i při přetížení sítě nebo částečných výpadcích. AEA podporuje jak vysílání v buňkách (cell broadcast), tak metody doručování založené na poloze, což umožňuje orgánům přesně cílit na konkrétní geografické oblasti při zachování zpětné kompatibility se staršími varovnými systémy, jako je Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System ([CMAS](/mobilnisite/slovnik/cmas/)).

Architektura AEA zahrnuje několik klíčových komponent pracujících v koordinaci. Alert Gateway slouží jako rozhraní mezi orgány veřejného varování a mobilní sítí, přijímá varovné zprávy a převádí je do standardizovaných formátů. Cell Broadcast Center ([CBC](/mobilnisite/slovnik/cbc/)) spravuje distribuci varování v přístupové rádiové síti, zatímco Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G koordinuje spolupráci se základnovými stanicemi (eNBs/gNBs) pro vysílání zpráv prostřednictvím System Information Blocks (SIBs). User Equipment (UE) obsahuje vyhrazené AEA klienty, kteří monitorují varovné zprávy, zpracovávají je podle profilů předplatného a prezentují je uživatelům prostřednictvím vizuálních, zvukových a hmatových oznámení.

Zprávy AEA dodržují strukturovaný formát definovaný ve specifikacích 3GPP a obsahují povinné prvky, jako je identifikátor zprávy, sériové číslo, typ varování, stupeň závažnosti a geografický rozsah. Volitelné prvky mohou zahrnovat multimediální přílohy, vícejazyčný obsah a pokyny k akci. Systém podporuje více kategorií varování včetně přírodních katastrof (zemětřesení, tsunami, hurikány), technologických hrozeb (úniky chemikálií, jaderné incidenty), ohrožení veřejné bezpečnosti (teroristické útoky, aktivní střelci) a mimořádných událostí s únosem dítěte (AMBER alerts). Mechanismy doručování zahrnují okamžité vysílání pro časově kritická varování, naplánované vysílání pro varování předem a opakované přenosy pro zajištění přijetí zprávy.

Technická implementace AEA využívá několik mechanismů pro zajištění spolehlivosti a efektivity. Priorizace zpráv zajišťuje, že varování o mimořádných událostech získají síťové zdroje před běžným provozem, zatímco detekce duplicit zabraňuje tomu, aby uživatelé obdrželi stejné varování vícekrát. Geografické cílení využívá polygony na základě buněk nebo kruhové oblasti definované středovým bodem a poloměrem, přičemž síť vypočítá, které buňky spadají do postižené oblasti. Bezpečnostní prvky zahrnují digitální podpisy pro ověření zdroje varování a šifrování pro ochranu integrity zprávy. Systém také podporuje funkce přístupnosti, jako je převod textu na řeč pro uživatele se zrakovým postižením a vibrační vzory pro osoby se sluchovým postižením.

## K čemu slouží

AEA byl vyvinut za účelem řešení kritických nedostatků starších systémů pro varování v mimořádných událostech, zejména jejich omezené geografické přesnosti, nedostatku multimediálních schopností a závislosti na specifických síťových podmínkách. Tradiční varovné systémy jako ETWS a [CMAS](/mobilnisite/slovnik/cmas/), ačkoliv užitečné, nabízely především textová varování s hrubým geografickým cílením (často na úrovni okresu) a omezenou podporu moderních komunikačních potřeb. Rostoucí četnost a závažnost přírodních katastrof spolu s rostoucím veřejným očekáváním včasných a přesných informací o mimořádných událostech vytvořily poptávku po sofistikovanějším varovném systému, který by mohl využívat pokročilé možnosti buněčných sítí.

Vytvoření AEA bylo motivováno několika reálnými incidenty, u kterých se stávající varovné systémy ukázaly jako nedostatečné. Během velkých katastrof, jako jsou hurikány, lesní požáry a zemětřesení, potřebovaly orgány předat podrobné evakuační trasy, umístění úkrytů a bezpečnostní pokyny, které nemohly být efektivně komunikovány pouze prostřednictvím krátkých textových zpráv. Navíc rostoucí penetrace chytrých telefonů vytvořila příležitost pro doručování bohatého multimediálního obsahu včetně map, obrázků a videí, což by mohlo významně zlepšit reakci veřejnosti na mimořádné události. Systém také řeší problém dosažení přechodné populace, jako jsou turisté nebo dojíždějící, kteří nemusí být přihlášeni k místním varovným službám, ale nacházejí se v postižených oblastech.

AEA řeší problém informačního přetížení během mimořádných událostí tím, že umožňuje přesné geografické cílení, které se vyhne zbytečným varováním pro nepostiženou populaci. Řeší také problémy přístupnosti podporou více formátů prezentace vhodných pro osoby se zdravotním postižením. Z pohledu sítě AEA poskytuje mechanismy pro zajištění doručení varování i při scénářích přetížení, kdy mohou být běžné komunikační kanály zahlceny. Standardizace systému napříč vydáními 3GPP zajišťuje interoperabilitu mezi různými síťovými operátory a dodavateli zařízení a vytváří konzistentní uživatelský zážitek bez ohledu na typ zařízení nebo předplatného.

## Klíčové vlastnosti

- Geografické cílení s definicemi polygonů a kruhových oblastí
- Podpora multimediálního obsahu včetně obrázků, zvuku a video příloh
- Více metod doručování (vysílání v buňkách, na základě polohy, IP-based)
- Zpětná kompatibilita se systémy ETWS a CMAS
- Autentizace digitálním podpisem a ochrana integrity zprávy
- Funkce přístupnosti pro uživatele se zdravotním postižením

## Související pojmy

- [CMAS – Commercial Mobile Alert Service](/mobilnisite/slovnik/cmas/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [AEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aea/)
