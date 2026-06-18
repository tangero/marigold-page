---
slug: "pno"
url: "/mobilnisite/slovnik/pno/"
type: "slovnik"
title: "PNO – Primary Network Operator"
date: 2025-01-01
abbr: "PNO"
fullName: "Primary Network Operator"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pno/"
summary: "Primární síťový operátor (PNO) je hlavní operátor odpovědný za poskytování síťových služeb uživateli v určité oblasti nebo pro konkrétní službu. Jde o klíčový koncept pro výběr sítě, roaming a kontinu"
---

PNO (primární síťový operátor) je hlavní operátor odpovědný za poskytování síťových služeb uživateli v určité oblasti nebo pro konkrétní službu.

## Popis

Primární síťový operátor (PNO) je konceptuální entita v rámci specifikací 3GPP, která identifikuje hlavního operátora odpovědného za předplatné uživatele a jeho primární přístup k síti. Nejde o fyzický síťový uzel, ale o logické označení používané v síťových politikách, datech předplatného a meziodběratelských dohodách. PNO je typicky domovský síťový operátor uživatele, který spravuje předplatné, poskytuje základní servisní profil, autentizační údaje a fakturační vztah. Tento koncept je klíčový pro definici „domovské“ sítě v protikladu k navštíveným sítím při roamingu.

Z architektonického hlediska je identita PNO uložena v profilu předplatného uživatele na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) nebo v [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management). Když se uživatelské zařízení (UE) pokouší připojit k síti, procedury objevování a výběru sítě (řízené specifikacemi jako TS 22.912 a TS 22.937) využívají informace o PNO k upřednostnění výběru sítě. Univerzální [SIM](/mobilnisite/slovnik/sim/) karta ([USIM](/mobilnisite/slovnik/usim/)) v UE obsahuje identifikátor domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)), který přímo odpovídá PNO. Algoritmy výběru sítě zajišťují, že se UE pokusí zaregistrovat v síti PNO jako první, kdykoli je dostupná, čímž garantují kontinuitu služeb a dodržování smluvních dohod.

Role PNO zasahuje do funkcí jádra sítě, jako je autentizace, autorizace a řízení politik. Během počáteční registrace se obsluhující síť spojí s domovskou sítí PNO, aby uživatele autentizovala pomocí protokolu [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement). Funkce [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) v síti PNO může uplatňovat specifická pravidla pro politiky a účtování na základě předplatného uživatele. V roamingových scénářích nese PNO konečnou odpovědnost za účastníka, i když navštívená veřejná pozemní mobilní síť ([VPLMN](/mobilnisite/slovnik/vplmn/)) poskytuje rádiový přístup a služby místního průniku. Koncept PNO je také nedílnou součástí architektur pro sdílení sítí, jako je MOCN (Multi-Operator Core Network) a GWCN (Gateway Core Network), kde více operátorů sdílí prostředky rádiové přístupové sítě, ale udržuje samostatná jádra sítí; v takových případech každý operátor vystupuje jako PNO pro své vlastní účastníky.

V pokročilých nasazeních, včetně neveřejných sítí 5G (NPN) a síťového řezání, se koncept PNO přizpůsobuje. Pro podnik nasazující privátní síť může být samotný podnik považován za PNO pro svou uzavřenou skupinu uživatelů. V rámci síťového řezání může být řez vytvořen a spravován konkrétním PNO, a to i v prostředí se sdílenou fyzickou infrastrukturou. PNO zůstává klíčovým ukotvením pro smlouvy o úrovni služeb (SLA), regulatorní shodu a správu služeb od konce ke konci napříč stále složitějšími a rozčleněnými síťovými architekturami.

## K čemu slouží

Koncept primárního síťového operátora byl zaveden, aby poskytl jasný a jednoznačný ukotvující bod pro vlastnictví účastníka a síťovou odpovědnost v ekosystému více operátorů. Před jeho formalizací byl výběr sítě a roaming silně závislý na identifikátoru HPLMN, ale rostoucí složitost sdílení sítí, národních roamingových dohod a virtuálních mobilních operátorů (MVNO) vyžadovala robustnější logický rámec. Označení PNO řeší problém identifikace „kdo je konečně odpovědný za účastníka“ ve scénářích, kde je síťová infrastruktura sdílena nebo kde se uživatel připojí k partnerské síti.

Historicky, jak se GSM vyvíjelo do 3G a LTE, operátoři začali sdílet infrastrukturu (jako jsou vysílače a rádiové vybavení), aby snížili náklady na nasazení, zejména ve venkovských oblastech. To vytvořilo scénáře, kdy zařízení uživatele mohlo detekovat více identifikátorů veřejné pozemní mobilní sítě (PLMN ID) z jediného rádiového vysílače. Koncept PNO, formalizovaný ve vydání 8 spolu s ranými pracemi na LTE, poskytl potřebnou logiku pro UE a síť, aby určily správného „domovského“ operátora pro registraci, autentizaci a vynucování politik. Řešil omezení, kdy prostý výběr založený na PLMN byl nedostatečný pro složité komerční a provozní modely, jako je síť jako služba.

Dále je rámec PNO nezbytný pro regulatorní shodu, zejména pro tísňové služby (např. E911), zákonné odposlechy a přenositelnost čísel. Regulátoři potřebují identifikovat odpovědného operátora pro hovor nebo datovou relaci účastníka. PNO slouží jako tato jednoznačná entita, která zajišťuje odpovědnost. Jeho vytvoření bylo motivováno potřebou škálovatelného, budoucím vývojem ovlivnitelného modelu, který by dokázal pojmout nejen tradiční mobilní operátory (MNO), ale také MVNO, operátory privátních sítí a neutrální hostitele, a to vše při zachování bezproblémového uživatelského zážitku a jasných provozních hranic.

## Klíčové vlastnosti

- Definuje domovského operátora odpovědného za předplatné účastníka a primární poskytování služeb.
- Slouží jako ukotvení pro procedury výběru sítě, což zajišťuje, že UE upřednostní připojení k síti PNO, pokud je dostupná.
- Působí jako kořen důvěry pro autentizaci, autorizaci a řízení politik v domácích i roamingových scénářích.
- Poskytuje jasnou entitu pro regulatorní odpovědnost, fakturaci a smlouvy o úrovni služeb.
- Přizpůsobuje se moderním síťovým architekturám včetně sdílení sítí (MOCN/GWCN), MVNO a neveřejných sítí.
- Je uložen v datech předplatného na HSS/UDM a v USIM zařízení UE jako domovská PLMN (HPLMN).

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)

## Definující specifikace

- **TR 22.912** (Rel-19) — Network Selection for Non-3GPP Access
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity

---

📖 **Anglický originál a plná specifikace:** [PNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/pno/)
