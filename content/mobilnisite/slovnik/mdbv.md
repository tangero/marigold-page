---
slug: "mdbv"
url: "/mobilnisite/slovnik/mdbv/"
type: "slovnik"
title: "MDBV – Maximum Data Burst Volume"
date: 2026-01-01
abbr: "MDBV"
fullName: "Maximum Data Burst Volume"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mdbv/"
summary: "Parametr kvality služeb (QoS) v 5G, který definuje největší množství dat, které musí systém 5G obsloužit v rámci přidružené Maximální doby trvání dávky (Maximum Burst Duration) identifikátoru QoS 5G ("
---

MDBV je největší množství dat, které musí systém 5G obsloužit v rámci přidružené Maximální doby trvání dávky (Maximum Burst Duration) toku QoS 5G, aby byla zaručena nízká latence a spolehlivost.

## Popis

Maximum Data Burst Volume (MDBV) je klíčový parametr v rámci modelu kvality služeb (QoS) v 5G, konkrétně přidružený k identifikátoru QoS 5G ([5QI](/mobilnisite/slovnik/5qi/)). Kvantifikuje v bajtech maximální množství dat, která musí síť zvládnout jako jednu dávku, a přitom stále splňovat záruky latence a spolehlivosti definované pro daný 5QI. MDBV funguje ve spojení s Maximální dobou trvání dávky (Maximum Burst Duration, MBD), která definuje časové okno pro tuto dávku. V zásadě musí být síť pro daný tok QoS navržena tak, aby zajistila, že dávka dat o velikosti až do hodnoty MDBV může být doručena během MBD bez porušení rozpočtu zpoždění paketu.

Technicky MDBV využívá plánovač paketů v rádiové přístupové síti (RAN) a mechanismy vynucování QoS ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). Při zřízení toku QoS jsou tyto síťové prvky informovány o přidruženém 5QI, který nese hodnotu MDBV (buď standardizovanou pro daný 5QI, nebo signalizovanou dynamicky). Plánovač tyto informace používá k alokaci rádiových prostředků. Například pro službu Ultra-Reliable Low Latency Communication (URLLC) je definována malá hodnota MDBV (např. odpovídající jedinému průmyslovému řídicímu příkazu) a velmi krátká MBD. Plánovač musí tyto pakety upřednostnit a zajistit okamžitou dostupnost dostatečných prostředků k vyřízení dávky v rámci přísného časového limitu.

Jeho role je zásadní pro tvorbu provozu (traffic shaping) a řízení přístupu (admission control). Funkce správy relace ([SMF](/mobilnisite/slovnik/smf/)) může použít MDBV během zřizování toku QoS k rozhodnutí, zda síť má dostatek prostředků pro přijetí nového toku s přísnými požadavky. V uživatelské rovině pomáhá zabránit situacím, kdy by velká, neočekávaná dávka dat mohla způsobit zpoždění ve frontách pro pakety citlivé na latenci. Definováním 'dávkovitosti' (burstiness), kterou služba může vykazovat, umožňuje MDBV síti plánovat alokaci prostředků přesněji než pouze s parametry průměrného přenosového výkonu, což je klíčové pro deterministický výkon vyžadovaný průmyslovým IoT, autonomními vozidly a hrami v reálném čase.

## K čemu slouží

MDBV byl zaveden, aby řešil přísné a deterministické požadavky na QoS nových případů užití v 5G, zejména Ultra-Reliable Low Latency Communication (URLLC) a průmyslového IoT. Předchozí generace mobilních sítí (4G/LTE) primárně používaly parametry jako garantovaný přenosový výkon ([GBR](/mobilnisite/slovnik/gbr/)) a maximální přenosový výkon ([MBR](/mobilnisite/slovnik/mbr/)), které jsou účinné pro kontinuální toky (jako je video), ale nedostačující pro charakterizaci dávkovitého provozu kritického na latenci. Garance konstantního přenosového výkonu nezajistí, že náhlá dávka dat bude doručena během několika milisekund.

Základní problém, který MDBV řeší, je poskytnutí kvantifikovatelné meze pro 'dávkovitost' (burstiness) služeb citlivých na latenci. Ve scénářích URLLC jsou přenosy dat často sporadické, ale musí být doručeny s extrémní spolehlivostí a minimálním zpožděním (např. 1 ms). Síť potřebuje znát maximální velikost takové dávky, aby si mohla rezervovat odpovídající prostředky (rádiové sloty, kapacitu zpracování) pro její okamžité vyřízení. Bez MDBV by síť buď nadměrně alokovala prostředky pro nejhorší případ kontinuálního výkonu (neefektivní), nebo by riskovala, že dávky nedoručí včas (nespolehlivé).

Jeho vytvoření bylo motivováno potřebou převést požadavky na úrovni aplikace (např. 'doručte 200bajtový paket do 5 ms se spolehlivostí 99,999 %') na konkrétní síťové parametry, na které mohou plánovače reagovat. MDBV spolu s MBD a rozpočtem zpoždění paketu (PDB) tvoří úplný model pro dávkovitý provoz citlivý na latenci. To umožňuje systémům 5G nabízet skutečné záruky výkonu, posouvat se od služeb typu 'best-effort' nebo 'prioritizovaných' k deterministické konektivitě, což je základním požadavkem vertikálních odvětví přijímajících 5G pro operace kritické pro misi.

## Klíčové vlastnosti

- Definuje horní mez objemu dat pro jednu dávku na tok QoS
- Používá se ve spojení s Maximální dobou trvání dávky (MBD) pro výpočty latence
- Klíčový parametr pro algoritmy plánovače paketů v RAN
- Umožňuje deterministickou rezervaci prostředků pro dávkovitý provoz
- Kritický pro splnění záruk služby Ultra-Reliable Low Latency Communication (URLLC)
- Může být standardizován pro každý 5QI nebo signalizován dynamicky během zřizování toku QoS

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [MDBV na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdbv/)
