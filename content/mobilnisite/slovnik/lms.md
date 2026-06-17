---
slug: "lms"
url: "/mobilnisite/slovnik/lms/"
type: "slovnik"
title: "LMS – Location Management Server"
date: 2026-01-01
abbr: "LMS"
fullName: "Location Management Server"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lms/"
summary: "Funkce jádrové sítě definovaná pro architekturu služeb určení polohy (LCS), odpovědná za správu a poskytování polohových dat a služeb. Funguje jako centrální úložiště a procesor pro informace o poloze"
---

LMS je funkce jádrové sítě, která spravuje a poskytuje polohová data, přičemž funguje jako centrální úložiště a procesor pro informace o poloze účastníka, nastavení ochrany soukromí a autorizaci služeb.

## Popis

Location Management Server (LMS) je funkční entita v architektuře služeb určení polohy ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP, zavedená jako součást širšího vývoje směrem k flexibilnějším a službami orientovaným jádrovým sítím. Je definována jako komponenta, kterou lze nasadit v rámci 5G Core (5GC) nebo přizpůsobit pro jiné architektury. LMS centralizuje správu polohových dat a logiky, která byla dříve rozptýlena mezi jinými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)). Jejím hlavním úkolem je ukládat a zpracovávat odběry polohových služeb, uživatelská nastavení ochrany soukromí (autorizace LCS klientů) a polohová data účastníka nebo odkazy na taková data.

Z architektonického hlediska LMS komunikuje s ostatními funkcemi jádrové sítě prostřednictvím službami orientovaných rozhraní (např. rozhraní Nlmf). Mezi klíčové interakce patří komunikace s funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) za účelem získání odhadů polohy z přístupové sítě, s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro data účastníka a s externími klienty služby určení polohy (např. od třetí strany nebo interní síťové služby). LMS může ukládat trvalé nebo dočasné polohové informace, definice geografických zón (geofencing) a spouštěcí události pro periodické nebo událostmi řízené hlášení polohy. Implementuje logiku pro vyhodnocování polohových spouštěčů a oznamování autorizovaným klientům při splnění podmínek.

Princip činnosti: Když LMS obdrží požadavek na polohu od autorizovaného LCS klienta, ověří jej proti profilu ochrany soukromí cílového uživatele. Pokud je požadavek autorizován, určí vhodnou metodu pro získání polohy. To může zahrnovat dotaz na AMF, který následně může iniciovat signalizaci s rádiovou přístupovou sítí (RAN) a UE (s použitím protokolů jako LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/))) za účelem vygenerování odhadu polohy pomocí [GNSS](/mobilnisite/slovnik/gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/) nebo jiných metod určování polohy. LMS následně naformátuje a vrátí polohovou informaci žádajícímu klientovi. U odložených nebo spouštěných požadavků na polohu LMS ukládá kritéria spouštěče a spravuje průběžné monitorování, iniciuje načítání polohy podle potřeby a zasílá oznámení. Centralizací této správy LMS zjednodušuje servisní logiku, zlepšuje škálovatelnost a poskytuje jednotný bod pro uplatňování zásad ochrany soukromí a smluv o úrovni služeb (SLA) pro polohové informace.

## K čemu slouží

LMS byla vytvořena, aby řešila rostoucí složitost a poptávku po službách založených na poloze v mobilních sítích, které daleko přesahovaly rámec základní lokalizace volajícího u tísňových služeb. Předchozí architektury LCS, soustředěné kolem GMLC, byly často monolitické a úzce provázané s prvky přepojování okruhů nebo raných paketových jader. Jak se sítě vyvíjely směrem k cloud-nativním, službami orientovaným architekturám (SBA) s 5GC, vznikla potřeba dekompozice funkcí pro větší flexibilitu, škálovatelnost a nezávislé inovace. LMS ztělesňuje tuto dekompozici tím, že vyčleňuje logiku správy polohy, odběrů a ochrany soukromí do dedikované, škálovatelné síťové funkce.

Toto oddělení řeší několik problémů: umožňuje efektivnější zpracování obrovského množství požadavků na polohu od zařízení IoT a komerčních aplikací; poskytuje jasné, standardizované rozhraní pro vývojáře aplikací pro přístup k síťovým polohovým schopnostem; a centralizuje kritickou funkci kontroly ochrany soukromí, která je stále důležitější kvůli regulacím jako GDPR. Vytvoření LMS bylo motivováno případy použití, jako jsou připojená vozidla, sledování majetku, výstrahy založené na poloze a vylepšené tísňové služby (např. Advanced Mobile Location), které vyžadují spolehlivý, nízkolatenční a zásadami řízený přístup k poloze zařízení. Umožňuje síťovým operátorům nabízet polohu jako spravovanou platformní službu s diferencovanými úrovněmi QoS a zabezpečení, často ve spojení s network slicing pro specifické vertikální odvětví.

## Klíčové vlastnosti

- Centralizovaná správa odběrů polohových služeb a uživatelských nastavení ochrany soukromí (LCS privacy)
- Podpora scénářů okamžitých, odložených a spouštěných požadavků na polohu
- Spolupráce s různými metodami určování polohy (UE-based, UE-assisted, network-based) prostřednictvím jádrové sítě
- Službami orientované rozhraní (např. Nlmf) pro integraci v architektuře 5G Core
- Ukládání a zpracování polohových dat a spouštěčů geografických zón (geofencing)
- Autorizace a vynucování politik pro externí a interní klienty služby určení polohy (Location Service Clients)

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks

---

📖 **Anglický originál a plná specifikace:** [LMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lms/)
