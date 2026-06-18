---
slug: "stmr"
url: "/mobilnisite/slovnik/stmr/"
type: "slovnik"
title: "STMR – SideTone Masking Rating"
date: 2025-01-01
abbr: "STMR"
fullName: "SideTone Masking Rating"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/stmr/"
summary: "STMR je standardizovaná metrika pro kvantifikaci kvality okruhu vlastního slyšení (sidetone) v telekomunikačním koncovém zařízení. Vlastní slyšení je řízená zpětná vazba uživatelova vlastního hlasu do"
---

STMR je standardizovaná metrika pro kvantifikaci kvality okruhu vlastního slyšení (sidetone) v telekomunikačním koncovém zařízení, která zajišťuje konzistentní kvalitu hlasu.

## Popis

SideTone Masking Rating (STMR) je psychoakustický parametr definovaný ve specifikacích 3GPP pro objektivní měření výkonu okruhu vlastního slyšení v koncovém zařízení, jako je mobilní telefon nebo VoIP sluchátko. Vlastní slyšení je záměrné zavedení přenášeného řečového signálu uživatele, zeslabeného a případně zpracovaného, zpět do přijímače (sluchátka). Tato akustická zpětná vazba je nezbytná, protože uživatelům poskytuje sluchové potvrzení, že jejich hlas je přenášen, a pomáhá jim regulovat hlasitost mluvení v různých podmínkách okolního hluku. Bez vlastního slyšení mají uživatelé tendenci mluvit příliš hlasitě v tichém prostředí nebo příliš potichu v hlučném, což vede k nepřirozené dynamice konverzace a potenciálnímu diskomfortu posluchače.

Technicky je STMR odvozeno z měření elektroakustických charakteristik terminálu. Proces zahrnuje aplikaci standardizovaného testovacího signálu (typicky šumu podobného řeči) na mikrofon zařízení a měření výsledného akustického výstupu na přijímači. Hodnota STMR, vyjádřená v decibelech (dB), kvantifikuje efektivní ztrátu nebo útlum okruhu vlastního slyšení. Vyšší hodnota STMR indikuje nižší úroveň vlastního slyšení (větší útlum), zatímco nižší hodnota indikuje vyšší úroveň vlastního slyšení. Měření zohledňuje celkovou kmitočtovou charakteristiku zařízení včetně mikrofonu, algoritmů digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) pro potlačení šumu a řízení ozvěny a akustických vlastností přijímače. Cílem je zajistit, aby úroveň vlastního slyšení byla v rozsahu, který je pro uživatele přirozený – dostatečná pro komfort konverzace, ale ne tak hlasitá, aby způsobovala nestabilitu (houkání) nebo maskovala hlas protistrany.

Role STMR v síťovém ekosystému je role zajištění kvality a interoperability. Zatímco generování vlastního slyšení je funkcí samotného terminálu, standardy 3GPP definují cílové rozsahy STMR, aby zajistily konzistentní uživatelský prožitek bez ohledu na výrobce telefonu nebo síťovou technologii (např. 2G, 3G, VoLTE). Síťoví operátoři a výrobci terminálů tyto specifikace používají během schvalování typu zařízení a testů shody. Dodržování požadavků na STMR pomáhá předcházet uživatelským stížnostem souvisejícím s kvalitou hlasu, jako je pocit mluvení do 'mrtvého' telefonu nebo nepříjemné ozvěny. Dále v kontextu Voice over LTE (VoLTE) a Voice over NR (VoNR), kde je hlas paketizován, hraje DSP terminálu klíčovou roli v řízení vlastního slyšení ve spojení s algoritmy akustického potlačení ozvěny ([AEC](/mobilnisite/slovnik/aec/)). Metrika STMR zajišťuje, že tyto složité řetězce digitálního zpracování stále poskytují základní, přirozený telefonní prožitek.

## K čemu slouží

Metrika STMR byla vytvořena, aby řešila základní výzvu v telefonii: replikaci přirozené akustické zpětné vazby přítomné v konverzaci tváří v tvář. V raných telefonních systémech se vlastní slyšení vyskytovalo přirozeně kvůli nedokonalé izolaci mezi mikrofonem a přijímačem v uhlíkovém telefonním sluchátku. S vývojem technologie směrem k elektronickým a později digitálním terminálům bylo toto akustické propojení eliminováno, aby se zabránilo nestabilitě a zlepšila se srozumitelnost hlasu. Jeho úplné odstranění však způsobilo, že telefon působil nepřirozeně a odpojeně, což vedlo uživatele k nepřirozenému způsobu mluvení. Účelem standardizace STMR bylo poskytnout objektivní, opakovatelnou metodu pro konstruktéry terminálů, aby mohli do systému navrhnout řízené, optimální množství elektronického vlastního slyšení.

Před standardizací byla implementace vlastního slyšení z velké části ponechána na uvážení výrobců zařízení, což vedlo k významné variabilitě uživatelského prožitku. Uživatel přecházející mezi různými modely telefonů mohl narazit na výrazné rozdíly v tom, jak 'živě' spojení působilo, což mohlo ovlivnit vnímanou kvalitu hovoru a spokojenost uživatele. Zavedení STMR v 3GPP Release 5 spolu s dalšími metrikami kvality hlasu formalizovalo tento aspekt výkonu terminálu. Vyřešilo problém nekonzistentní subjektivní kvality definováním měřitelného cíle. To bylo obzvláště důležité s globalizací mobilních komunikací, protože zajišťovalo, že telefon certifikovaný v jedné oblasti poskytne přijatelný základní hlasový prožitek v oblasti jiné. Řeší základní problém vyvážení potřeby jasného, bezozvěnového přenosu s požadavky lidského faktoru na komfort konverzace a přirozenou interakci.

## Klíčové vlastnosti

- Objektivní psychoakustické měření útlumu okruhu vlastního slyšení
- Standardizované testovací signály a měřicí postupy definované v 3GPP TS 26.131/132
- Vyjádřeno jako jednočíselné hodnocení v decibelech (dB)
- Zajišťuje konzistentní konverzační pocit napříč různými konstrukcemi terminálů
- Integrální součást testů akustické shody terminálu
- Podporuje kvalitu prožitku (QoE) pro hlasové služby

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [STMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/stmr/)
