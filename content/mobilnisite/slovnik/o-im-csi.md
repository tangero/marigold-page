---
slug: "o-im-csi"
url: "/mobilnisite/slovnik/o-im-csi/"
type: "slovnik"
title: "O-IM-CSI – Originating IP Multimedia CAMEL Subscription Information"
date: 2025-01-01
abbr: "O-IM-CSI"
fullName: "Originating IP Multimedia CAMEL Subscription Information"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-im-csi/"
summary: "Data předplatitele uložená v HSS, která S-CSCF instruují, kdy a jak vyvolat aplikační logiku služeb založených na CAMEL pro relace pocházející od daného uživatele. Obsahují adresu uzlu řízení služeb ("
---

O-IM-CSI je informace o předplatném pro službu CAMEL v IP multimediální subsystému pro odchozí relace (Originating IP Multimedia CAMEL Subscription Information). Jde o data předplatitele uložená v HSS, která S-CSCF instruují, kdy a jak vyvolat aplikační logiku služby CAMEL pro relace pocházející od daného uživatele.

## Popis

O-IM-CSI je klíčová sada dat specifických pro předplatitele v architektuře IMS podle 3GPP, která umožňuje poskytování operátorem definovaných, na síť orientovaných inteligentních služeb. Jedná se o typ informace o předplatném pro službu [CAMEL](/mobilnisite/slovnik/camel/) (CAMEL Subscription Information – [CSI](/mobilnisite/slovnik/csi/)) přizpůsobený pro IP multimediální subsystém (IMS). Tato data jsou trvale uložena v profilu uživatele na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) a jsou dynamicky stažena do funkce [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving Call Session Control Function) během procesu registrace uživatele v IMS nebo když S-CSCF potřebuje obsloužit odchozí relaci pro tohoto uživatele. O-IM-CSI funguje jako konfigurace neboli 'seznam spouštěčů', který personalizuje chování modelu [O-IM-BCSM](/mobilnisite/slovnik/o-im-bcsm/) (Originating IP Multimedia Basic Call State Model) pro daného předplatitele.

Informace obsažené v O-IM-CSI zahrnují především adresu gsmSCF (uzlu hostujícího aplikační logiku služby CAMEL, např. [SCP](/mobilnisite/slovnik/scp/)) a podrobný spouštěcí profil. Tento profil specifikuje, které detekční body (Detection Points – DPs) ve stavovém automatu O-IM-BCSM jsou pro tohoto předplatitele 'aktivovány'. Když S-CSCF při zpracování odchozí [SIP](/mobilnisite/slovnik/sip/) relace (např. zahájení hovoru) dosáhne aktivovaného [DP](/mobilnisite/slovnik/dp/), pozastaví běžné zpracování hovoru. Poté sestaví operaci protokolu CAP (CAMEL Application Part), například InitialDP, a odešle ji na adresu gsmSCF uvedenou v O-IM-CSI. gsmSCF vykoná svou aplikační logiku – která může zahrnovat dotazování databází, aplikaci tarifních pravidel nebo úpravu parametrů hovoru – a pošle zpět instrukce pro S-CSCF, jak pokračovat.

Z architektonického hlediska je O-IM-CSI klíčovou součástí rámce řízení služeb IMS, stojící na průsečíku správy dat předplatitelů (HSS), řízení relací (S-CSCF) a provádění služeb (gsmSCF). Její úlohou je dynamicky propojit předplatitele s jeho předplacenými službami. Bez O-IM-CSI by S-CSCF nevědělo, kteří předplatitelé vyžadují interakci s CAMEL, a zpracovávalo by všechny hovory pomocí výchozích, neinteligentních procedur. Je základním prvkem umožňujícím personalizované služby, jako je předplacená služba v IMS, zákaz odchozích hovorů, řešení přenositelnosti čísel nebo spouštěče pro zákonné odposlechy pro odchozí relace. Data jsou přenášena z HSS do S-CSCF přes rozhraní Cx pomocí protokolu Diameter.

## K čemu slouží

O-IM-CSI bylo vytvořeno za účelem poskytnutí mechanismu specifického pro předplatitele pro inteligentní spouštění služeb v IMS, což zrcadlí úspěšný koncept CSI z okruhově spínané domény GSM/UMTS. V sítích před érou IMS umožňovalo O-CSI (Originating CSI) MSC vyvolávat služby pro odchozí okruhově spínané hovory. S vývojem sítí směrem k IMS vznikla jasná potřeba ekvivalentní datové struktury, která by fungovala se SIP-based O-IM-BCSM v S-CSCF. Účelem O-IM-CSI je oddělit aplikační logiku služeb od základního řízení relací, což umožňuje flexibilní a personalizované nasazování služeb.

Řeší problém, jak efektivně a dynamicky informovat kontrolér relací (S-CSCF) o tom, kteří uživatelé mají které inteligentní služby, a přesně kdy během sestavování hovoru mají být tyto služby vyvolány. Bez takové standardizované datové struktury by spouštění služeb vyžadovalo statickou konfiguraci v síťových prvcích nebo by bylo nemožné, což by vážně omezilo agilitu služeb. O-IM-CSI umožňuje operátorům definovat služby centrálně (na gsmSCF) a pro jejich aktivaci nebo úpravu jednoduše aktualizovat profily předplatitelů v HSS, aniž by bylo nutné rekonfigurovat každé S-CSCF v síti. Jeho vytvoření bylo motivováno požadavky na hromadné přizpůsobení služeb, rychlé poskytování služeb a bezproblémovou migraci milionů stávajících předplatných služeb CAMEL z okruhově spínaného prostředí do prostředí IMS.

## Klíčové vlastnosti

- Uloženo v HSS jako součást profilu předplatitele IMS
- Staženo do S-CSCF přes rozhraní Cx pomocí protokolu Diameter
- Obsahuje adresu uzlu řízení služeb gsmSCF
- Definuje spouštěcí profil aktivovaných detekčních bodů pro O-IM-BCSM
- Umožňuje specifické pro předplatitele vyvolání služeb CAMEL pro odchozí IMS relace
- Základní prvek pro personalizované služby, jako je předplacená služba v IMS a screening odchozích hovorů

## Související pojmy

- [T-IM-CSI – Terminating IP Multimedia CAMEL Subscription Information](/mobilnisite/slovnik/t-im-csi/)
- [O-IM-BCSM – Originating IP Multimedia Basic Call State Model](/mobilnisite/slovnik/o-im-bcsm/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [O-IM-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-im-csi/)
