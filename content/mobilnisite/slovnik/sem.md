---
slug: "sem"
url: "/mobilnisite/slovnik/sem/"
type: "slovnik"
title: "SEM – Spectrum Emissions Mask"
date: 2025-01-01
abbr: "SEM"
fullName: "Spectrum Emissions Mask"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sem/"
summary: "Maska spektrálních emisí (SEM) je regulační a standardizovaná šablona definující maximální přípustný výkon, který může rádiový vysílač vyzařovat mimo svou přidělenou šířku kanálu. Omezuje nežádoucí em"
---

SEM je regulační šablona definující maximální přípustný výkon vysílače mimo přidělený kanál za účelem omezení nežádoucích emisí a zabránění rušení jiných služeb.

## Popis

Maska spektrálních emisí (SEM) je klíčový technický parametr v normách pro rádiovou komunikaci, včetně specifikací 3GPP pro LTE a 5G NR. Je definována jako soubor limitů pro výkonovou spektrální hustotu, kterou může vysílač uživatelského zařízení (UE) nebo základnové stanice (gNB/[eNB](/mobilnisite/slovnik/enb/)) vyzařovat na frekvenčních odstupech od středu přidělené nosné. Maska je graficky znázorněna jako závislost s relativním výkonem (v dB) na ose Y a frekvenčním odstupem (v MHz nebo kHz) od okraje kanálu na ose X. Maska se typicky skládá z několika oblastí: definované 'šířky kanálu', kde se nachází užitečný signál, oblasti 'mimopásmových' (OOB) emisí bezprostředně přiléhající ke kanálu a oblasti 'parazitních emisí' ve větší vzdálenosti. Každá oblast má specifický limit, často definovaný vzhledem k maximálnímu výstupnímu výkonu vysílače nebo v absolutních jednotkách výkonu (např. dBm/MHz).

Měření shody s SEM je klíčovou součástí testování shody. Provádí se pomocí spektrálního analyzátoru nebo specializovaného testovacího zařízení. Testované zařízení vysílá standardizovaný referenční měřicí kanál ([RMC](/mobilnisite/slovnik/rmc/)) na maximální výkon. Naměřená výkonová spektrální hustota je následně integrována přes specifické měřicí šířky pásma (např. 1 MHz pro větší odstup) na předepsaných frekvenčních odstupech a porovnána s limity uvedenými v příslušné specifikaci 3GPP (např. TS 36.101 pro LTE UE, TS 38.101 pro NR UE). SEM se uplatňuje na kombinované emise všech aktivních komponentních nosných ve scénářích s agregací nosných, čímž zajišťuje, že agregovaný signál nepřekračuje masku.

SEM funguje v součinnosti s dalšími požadavky na vysílač, jako je poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a parazitní emise. Zatímco ACLR je jednodušší dvoubodové měření úniku výkonu do bezprostředně sousedního kanálu, SEM poskytuje komplexnější a podrobnější profil emisí v širokém frekvenčním rozsahu. Její vynucování zajišťuje, že neideální charakteristiky vysílače – jako nelinearita výkonového zesilovače, fázový šum a nedokonalý sklon filtru – negenerují nadměrné rušení. Provozovatelé sítí se spoléhají na dodržování SEM, aby zajistili, že miliony zařízení mohou pracovat současně bez degradace výkonu navzájem, což umožňuje efektivní opakované využití spektra a vysokou kapacitu sítě.

## K čemu slouží

Maska spektrálních emisí existuje za účelem umožnění uspořádaného a nerušeného sdílení rádiového frekvenčního spektra, což je omezený a přísně regulovaný veřejný zdroj. Bez přísné kontroly nežádoucích emisí vysílače by zařízení pracující na jednom frekvenčním kanálu způsobovalo nepřijatelné rušení přijímačům na sousedních kanálech, a to jak ve stejné síti, tak v jiných spoluumístěných nebo přilehlých rádiových službách (např. jiná mobilní pásma, letectví, [GPS](/mobilnisite/slovnik/gps/)). To by drasticky snížilo kapacitu systému a kvalitu služeb.

Historicky, jak se rádiová technologie vyvíjela od jednoduché analogové ke složité digitální modulaci se širokými šířkami pásma (jako je [OFDM](/mobilnisite/slovnik/ofdm/) v LTE a NR), potenciál pro spektrální regeneraci a mimopásmové emise vzrostl. Dřívější, méně přísné limity se ukázaly jako nedostatečné. SEM byla vyvinuta jako přesný, standardizovaný nástroj pro regulátory (jako [FCC](/mobilnisite/slovnik/fcc/), [ETSI](/mobilnisite/slovnik/etsi/)) a normalizační orgány (3GPP) k definování 'spektrální stopy' vysílače. Řeší omezení přístupů založených na jediné metrice tím, že poskytuje detailní obrys přijatelných emisí. To umožňuje těsnější uspořádání kanálů vedle sebe (zlepšení spektrální účinnosti) při zachování záruk koexistence. Její vytvoření bylo motivováno potřebou škálovatelné, na technologii nezávislé metody pro specifikaci shody spektra vysílače, která by se mohla přizpůsobit různým šířkám kanálu, frekvenčním pásmům a scénářům nasazení.

## Klíčové vlastnosti

- Definuje maximální povolenou výkonovou spektrální hustotu na specifických frekvenčních odstupech od nosné
- Skládá se z více oblastí: nežádoucí emise v pracovním pásmu, oblast mimopásmových emisí a oblast parazitních emisí
- Specifikována samostatně pro základnové stanice a uživatelská zařízení (UE) v různých frekvenčních pásmech
- Měření je povinné pro testování rádiové shody a typové schválení
- Aplikuje se na agregované emise ve scénářích vysílání s více nosnými (CA) a více RAT
- Limity jsou často definovány vzhledem k maximálnímu výstupnímu výkonu vysílače (dBc) nebo v absolutních jednotkách (dBm/MHz)

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.833** — 3GPP TR 36.833
- **TS 37.809** (Rel-11) — E-UTRA & MSR BS Class Requirements
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TR 37.829** (Rel-18) — Technical Report
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TS 38.755** (Rel-19) — NR FR1 DL Fragmented Carriers Study
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [SEM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sem/)
