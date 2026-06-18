---
slug: "mpr"
url: "/mobilnisite/slovnik/mpr/"
type: "slovnik"
title: "MPR – Allowed Maximum Power Reduction"
date: 2025-01-01
abbr: "MPR"
fullName: "Allowed Maximum Power Reduction"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mpr/"
summary: "MPR je regulační a konstrukční parametr definující maximální hodnotu, o kterou může být vysílací výkon UE snížen pod jeho jmenovité maximum, aby byly splněny limity nežádoucích emisí. Zajišťuje, že za"
---

MPR (Allowed Maximum Power Reduction) je maximální hodnota, o kterou může být vysílací výkon uživatelského zařízení snížen pod jeho jmenovitý maximální výkon, aby bylo zajištěno dodržení limitů nežádoucích emisí, jako jsou spektrální maska a požadavky na poměr úniku do sousedního kanálu (ACLR).

## Popis

Allowed Maximum Power Reduction (MPR) je klíčový parametr definovaný v 3GPP specifikacích pro rádiové rozhraní (zejména pro uživatelská zařízení - UE), který řídí vztah mezi konfigurovaným výstupním výkonem zařízení a nezbytným snížením pro dodržení regulačních limitů emisí. Jmenovitý maximální výstupní výkon pro danou výkonovou třídu UE (např. 23 dBm pro mnohé mobilní přístroje) je definován za ideálních referenčních podmínek. V reálném provozu však, když UE vysílá pomocí určitých modulačních schémat (jako [64QAM](/mobilnisite/slovnik/64qam/) nebo 256QAM) nebo specifických alokací bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)), generuje signály s vyšším poměrem špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)). Tyto signály s vysokým PAPR mohou způsobit zvýšené spektrální rozrůstání a nežádoucí emise, což může vést k překročení přísných limitů spektrální emisní masky ([SEM](/mobilnisite/slovnik/sem/)) a poměru úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) stanovených regulátory pro ochranu sousedních kanálů a systémů. MPR definuje maximální hodnotu, o kterou je UE *oprávněna* snížit svůj vysílací výkon oproti jmenovitému maximu, aby tyto nežádoucí emise zůstaly v povolených mezích. Nejde o povinné snížení, ale o povolenou hodnotu; implementace v UE se může rozhodnout snížit výkon až na tuto hodnotu MPR. Skutečně aplikované snížení výkonu je často součástí algoritmu řízení výkonu UE. Hodnota MPR je funkcí řádu modulace, počtu přidělených souvislých nebo nesouvislých bloků zdrojů (PRB) a konkrétního kmitočtového pásma. Specifikace poskytují podrobné tabulky mapující tyto přenosové parametry na příslušnou hodnotu MPR. Tento mechanismus zajišťuje, že ani na nejvyšších konfigurovaných úrovních výkonu nelinearita vysílače UE nezpůsobí nepřijatelné rušení. Síťové plánovací algoritmy mohou také brát v potaz důsledky MPR, protože naplánování přenosu pro UE s konfigurací vyžadující vysoký MPR (např. vysoká modulace [QAM](/mobilnisite/slovnik/qam/) na okraji buňky) může mít za následek nižší efektivní vyzařovaný výkon a potenciálně nižší přenosové rychlosti.

## K čemu slouží

MPR existuje k vyřešení základního konfliktu mezi dosažením vysokých přenosových rychlostí a dodržením přísných regulačních požadavků na rádiové emise. Vysoce účinná modulační schémata jako [64QAM](/mobilnisite/slovnik/64qam/) a 256QAM jsou nezbytná pro spektrální efektivitu, ale produkují signály s vysokým poměrem špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)). Když jsou tyto signály s vysokým PAPR zesíleny nelineárním výkonovým zesilovačem v UE, způsobují spektrální rozrůstání, které šíří energii do sousedních kmitočtových kanálů. Bez kontroly by to způsobilo škodlivé rušení ostatním uživatelům. Účelem MPR je poskytnout standardizovanou, kvantifikovanou metodu pro UE, jak tento kompromis řídit. Řeší omezení přenosu s pevným výkonem tím, že umožňuje inteligentní snížení výkonu na základě podmínek. Historicky, jak se 3GPP vyvíjelo od LTE Rel-8 s jednoduššími modulacemi (QPSK, 16QAM) k pozdějším verzím s 64QAM, 256QAM a agregací nosných, rostl potenciál pro nadměrné nežádoucí emise. MPR byl zaveden, aby výrobcům UE poskytl jasnou cestu ke shodě: při použití těchto pokročilých funkcí mohou snížit výkon, aby udržely emise v mezích. To je praktičtější a nákladově efektivnější než vyžadovat, aby všechna UE měla ultra-lineární výkonové zesilovače schopné zpracovat jakýkoli signál na plný výkon, což by bylo neefektivní a zvýšilo by náklady, velikost a spotřebu baterie zařízení. MPR tedy umožňuje nasazení vysokorychlostních funkcí při současném zajištění, že rádiový ekosystém zůstane bez rušení.

## Klíčové vlastnosti

- Definuje přípustné snížení výkonu pro splnění požadavků SEM a ACLR
- Hodnota je určena řádem modulace (QPSK, 16QAM, 64QAM, 256QAM)
- Závisí na počtu a souvislosti přidělených bloků fyzických zdrojů (PRB)
- Specifikováno pro každé kmitočtové pásmo a konfiguraci přenosové šířky pásma
- Umožňuje použití vysoce účinných modulací při současné kontrole rušení
- Integrováno do úvah o řízení výkonu UE a síťovém plánování

## Související pojmy

- [ACL – Asynchronous Connection-Oriented Link](/mobilnisite/slovnik/acl/)
- [PAPR – Peak-to-Average Power Ratio](/mobilnisite/slovnik/papr/)

## Definující specifikace

- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.833** — 3GPP TR 36.833
- **TS 37.716** — 3GPP TR 37.716
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TS 37.825** (Rel-16) — High Power UE (PC2) for EN-DC TDD-TDD
- **TR 37.829** (Rel-18) — Technical Report
- **TS 37.872** (Rel-15) — Technical Report on SUL & LTE-NR DC with SUL
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [MPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpr/)
