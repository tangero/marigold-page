---
slug: "nua"
url: "/mobilnisite/slovnik/nua/"
type: "slovnik"
title: "NUA – Network User Access"
date: 2025-01-01
abbr: "NUA"
fullName: "Network User Access"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nua/"
summary: "Network User Access (NUA) je standardizovaný termín ve specifikacích 3GPP, používaný primárně v kontextu definic slovní zásoby. Odkazuje na mechanismy a procedury, kterými uživatel nebo uživatelovo za"
---

NUA je standardizovaný 3GPP termín pro mechanismy a procedury, kterými uživatel nebo uživatelské zařízení získá vstup do sítě.

## Popis

Network User Access (NUA) je konceptuální termín definovaný ve specifikacích 3GPP, nejvýznamněji v TS 21.905, což je dokument slovní zásoby pro 3GPP. Slouží jako standardizované označení pro nadřazený proces, při kterém se uživatel nebo uživatelské zařízení (UE) připojí k mobilní síti. Přestože NUA samo o sobě není konkrétním protokolem nebo architekturou, zahrnuje celý soubor procedur, od počátečního rádiového kontaktu po autentizaci a autorizaci, které vyústí ve vstup do sítě.

Termín poskytuje vysokou úroveň abstrakce pro komplexní interakce mezi UE a jádrem sítě (CN) a rádiovou přístupovou sítí (RAN). Implicitně zahrnuje klíčové procesy, jako je výběr a převýběr buňky, náhodný přístup, registrace a provádění procedur Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), jako je Attach nebo Registration. Definováním NUA zajišťuje 3GPP, že všechny následné technické diskuse o 'přístupu' odkazují na konzistentní a dobře pochopený koncept, což snižuje nejednoznačnost ve vývoji standardů.

V síťové architektuře NUA není komponentou, ale funkcí, která zahrnuje více síťových entit. Na straně UE zahrnuje modem a protokolový zásobník. Na straně sítě zapojuje gNodeB (v 5G) nebo eNodeB (v 4G) pro rádiové procedury a funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G nebo entitu Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G pro procedury jádra sítě, jako je autentizace a zřizování relace. Úspěšné dokončení NUA je předpokladem pro jakýkoli přenos dat v uživatelské rovině nebo využití služby.

Jeho role je zásadní; bez úspěšného Network User Access nelze poskytnout žádnou mobilní komunikační službu. Je to bránová funkce, která ověřuje uživatelský účet, zakládá jeho kontext v síti a alokuje potřebné zdroje. Přestože podrobné implementace jsou specifikovány v jiných technických specifikacích (např. pro protokoly NAS a [RRC](/mobilnisite/slovnik/rrc/)), NUA zůstává zastřešujícím termínem, který tyto implementace spojuje pod jediným, jasným cílem: udělit uživateli přístup k síti.

## K čemu slouží

Primárním účelem definování termínu Network User Access (NUA) jako standardizovaného pojmu je vytvoření společné slovní zásoby v rozsáhlém ekosystému specifikací 3GPP. Před jeho formální definicí mohly být diskuse o 'přístupu' interpretovány různě – rádiový přístup, přístup k jádru sítě, přístup ke službám – což vedlo k možným nedorozuměním mezi inženýry a přispěvateli standardů. Vytvořením přesného termínu chtěl 3GPP zlepšit srozumitelnost a konzistenci své technické dokumentace.

Historicky, jak se mobilní sítě vyvíjely od GSM přes UMTS a dále, se procedury pro vstup do sítě stávaly stále komplexnějšími a zahrnovaly více síťových funkcí a bezpečnostních kroků. Vznikl požadavek na koncept vysoké úrovně, na který by bylo možné odkazovat napříč různými pracovními skupinami (např. RAN, [SA](/mobilnisite/slovnik/sa/), [CT](/mobilnisite/slovnik/ct/)), aniž by se bylo nutno ponořovat do implementačních specifik jednotlivých releasů. NUA plní tento referenční účel a slouží jako konceptuální kotva.

Řeší problém terminologické nejednoznačnosti. Když specifikace uvádí, že funkce ovlivňuje 'Network User Access', okamžitě tím sděluje, že funkce ovlivňuje počáteční fázi připojení, potenciálně zahrnující řízení rádiových prostředků, registraci a autentizaci. To umožňuje efektivnější návrh a revizi specifikací, protože všechny strany sdílejí základní porozumění tomu, o které fázi provozu se jedná. Nezavádí novou technologii, ale poskytuje jazykový rámec pro koherentní popis stávajících a budoucích přístupových technologií.

## Klíčové vlastnosti

- Standardizovaný termín pro procedury vstupu do sítě
- Zahrnuje aspekty rádiového přístupu i přístupu k jádru sítě
- Poskytuje společný referenční bod v dokumentaci 3GPP
- Abstrahuje složitost podkladových protokolů, jako jsou NAS a RRC
- Základní předpoklad pro poskytnutí jakékoli mobilní služby
- Definován ve specifikaci slovní zásoby 3GPP TS 21.905

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nua/)
