---
slug: "momt"
url: "/mobilnisite/slovnik/momt/"
type: "slovnik"
title: "MOMT – Mobile Originated Mobile Terminated"
date: 2025-01-01
abbr: "MOMT"
fullName: "Mobile Originated Mobile Terminated"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/momt/"
summary: "Služební kategorie v 3GPP pro komunikaci, kde jsou jak iniciující, tak přijímající stranou mobilní uživatelé. Je základním prvkem pro umožnění přímých hovorů a zpráv mezi mobilními zařízeními a tvoří"
---

MOMT je služební kategorie 3GPP pro přímou komunikaci mezi mobilními účastníky, kde jsou jak iniciující, tak přijímající stranou mobilní uživatelé.

## Popis

Mobile Originated Mobile Terminated (MOMT) je základní služební kategorie definovaná v rámci servisního modelu 3GPP, podrobně specifikovaná např. v dokumentech TS 22.262 (Service Requirements) a TS 23.554 (Architecture). Popisuje kompletní scénář komunikace od konce ke konci, kde uživatelské zařízení (UE) iniciuje relaci (Mobile Originated, [MO](/mobilnisite/slovnik/mo/)) směrem k jinému UE, které je cílovým příjemcem (Mobile Terminated, [MT](/mobilnisite/slovnik/mt/)). To zahrnuje kompletní navázání signalizační a uživatelské cesty mezi dvěma mobilními účastníky. Architektonicky služby MOMT spoléhají na funkce řízení hovorových relací v jádru sítě, správu mobility a správu dat účastníků (např. v [HSS](/mobilnisite/slovnik/hss/)) pro správné směrování relace. Proces zahrnuje připojení iniciujícího UE k síti, provedení autorizace služby a zahájení žádosti o navázání relace (jako je [SIP](/mobilnisite/slovnik/sip/) INVITE pro hovory založené na IMS). Síť následně zjišťuje informace pro směrování, často za použití dotazů na HSS k lokalizaci cílového UE, a doručí žádost o relaci cílovému UE, které odpoví k dokončení navázání. Pro ne-IMS služby s okruhovým přepojováním platí podobné principy prostřednictvím [MSC](/mobilnisite/slovnik/msc/) serverů. MOMT není protokol, ale charakterizace služby, která určuje, jak síťové funkce jako [P-CSCF](/mobilnisite/slovnik/p-cscf/), [S-CSCF](/mobilnisite/slovnik/s-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/), MME, AMF a SMF interagují, aby splnily servisní logiku pro komunikaci mezi mobilními účastníky. Její role je klíčová pro definici účtování, práva na odposlech a politik kvality služby specifických pro tento nejběžnější komunikační vzor.

## K čemu slouží

Služební kategorie MOMT existuje k formální definici a standardizaci požadavků a architektonického chování pro nejzákladnější mobilní službu: přímou komunikaci mezi dvěma mobilními účastníky. Před zavedením komplexních servisních definic se implementace mohly lišit, což vedlo k problémům s interoperabilitou mezi různými síťovými operátory a dodavateli zařízení. Vytvořením standardizovaného popisu služby 3GPP zajišťuje, že hovor nebo zpráva iniciovaná z mobilního telefonu a určená jinému mobilnímu telefonu se chová konzistentně napříč globálními sítěmi. Tím se řeší problémy související s transparentností služeb, kompatibilitou roamingu a konzistentními účtovacími mechanismy. Historicky, jak se sítě vyvíjely od okruhově přepínaných 2G/3G k paketově přepínaným 4G/5G s IMS, stala se potřeba jasné, na přístupu nezávislé definice této základní služby klíčovou pro zajištění zpětné kompatibility a bezproblémového uživatelského zážitku. Řeší omezení plynoucí z vložení servisní logiky proprietárním způsobem do síťových uzlů a místo toho poskytuje referenční model pro implementaci služeb, který podporuje inovace na stabilním základě.

## Klíčové vlastnosti

- Definuje signalizační tok od konce ke konci pro relace od mobilního iniciátora k mobilnímu příjemci
- Podporuje jak modely hovorů založené na IMS (VoLTE, VoNR), tak i starší modely s okruhovým přepojováním
- Integruje se s procedurami lokalizace a směrování účastníka (např. dotaz na HSS/UDM)
- Tvoří základ pro generování účtovacích dat (např. pro hovory MO-MT)
- Umožňuje konzistentní aplikaci řízení politik (např. QoS, zákazy) pro tuto službu
- Poskytuje rámec pro právo na odposlech pro komunikaci mezi mobilními účastníky

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.262** (Rel-19) — MSGin5G Service Requirements
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture

---

📖 **Anglický originál a plná specifikace:** [MOMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/momt/)
