---
slug: "r-gmlc"
url: "/mobilnisite/slovnik/r-gmlc/"
type: "slovnik"
title: "R-GMLC – Requesting Gateway Mobile Location Centre"
date: 2025-01-01
abbr: "R-GMLC"
fullName: "Requesting Gateway Mobile Location Centre"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/r-gmlc/"
summary: "Entita jádra sítě v architektuře služeb určování polohy (LCS) pro LTE/5G, která slouží jako vstupní bod pro klienta. Přijímá požadavky na polohu od externích aplikací služeb založených na poloze (LBS)"
---

R-GMLC je síťová entita jádra sítě, která slouží jako vstupní bod pro externí aplikace služeb určování polohy. Autentizuje jejich požadavky a předává je do sítě, aby získala polohu cílového zařízení.

## Popis

Requesting Gateway Mobile Location Centre (R-GMLC) je klíčový funkční prvek v rámci standardizované architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP, zavedený společně s řešením určování polohy v řídicí rovině pro LTE. Slouží jako brána mezi externími klienty služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)) – známými jako LCS Clients – a interní infrastrukturou pro určování polohy v mobilní síti. R-GMLC se typicky nachází v domovské síti účastníka. Jeho primární funkcí je být prvním kontaktním bodem pro příchozí požadavek na polohu a obstarávat všechny aspekty transakce směrem ke klientovi.

Operačně R-GMLC přijímá standardizovaný požadavek na službu určení polohy (např. pomocí protokolů [MLP](/mobilnisite/slovnik/mlp/) nebo [SUPL](/mobilnisite/slovnik/supl/)) od externího LCS Clienta. Nejprve provádí klíčové síťové přístupové funkce: autentizuje LCS Clienta pro ověření jeho identity, autorizuje požadavek proti profilu soukromí cílového účastníka (kontroluje nastavení soukromí LCS uložená v [HSS](/mobilnisite/slovnik/hss/)) a může zpracovávat spouštěče účtování. Jakmile je požadavek ověřen, R-GMLC rozhodne o jeho směrování. Pokud je cílové uživatelské zařízení (UE) v roamingu, R-GMLC předá požadavek Gateway Mobile Location Centre v navštívené síti ([V-GMLC](/mobilnisite/slovnik/v-gmlc/)). Pokud je UE ve své domovské síti, může R-GMLC předat požadavek přímo Home Gateway Mobile Location Centre ([H-GMLC](/mobilnisite/slovnik/h-gmlc/)) nebo v některých architekturách převzít roli H-GMLC sám. R-GMLC se přímo nepodílí na výpočtech polohy; místo toho orchestruje požadavek sítí a nakonec přijímá odhad polohy (např. zeměpisné souřadnice) od síťové strany [GMLC](/mobilnisite/slovnik/gmlc/) (H-GMLC nebo E-SMLC přes MME). Tento výsledek pak naformátuje podle typu odpovědi požadované klientem a odešle jej zpět externímu LCS Clientovi.

Z architektonického hlediska R-GMLC komunikuje s HSS (pro data o soukromí účastníka), dalšími GMLC (přes rozhraní Lg) a externími LCS Clienty. Jeho role je klíčová pro škálovatelnost a bezpečnost, protože centralizuje autentizaci klientů, ověřování pravidel soukromí a směrování požadavků, čímž chrání interní síťové prvky před přímým externím přístupem. V systémech 5G analogickou funkci plní Location Management Function (LMF) ve spolupráci s Network Exposure Function (NEF), ale R-GMLC zůstává klíčovým konceptem ve vývoji určování polohy v řídicí rovině.

## K čemu slouží

R-GMLC byl zaveden, aby formalizoval a zabezpečil rozhraní mezi externími poskytovateli služeb a síťovými možnostmi určování polohy v LTE. Před jeho explicitní definicí architektury určování polohy, jako byly ty v GSM a UMTS, často kombinovaly bránové funkce v jediném uzlu GMLC. Oddělení role Requesting GMLC bylo motivováno potřebou jasnějšího architektonického oddělení, zvýšené bezpečnosti a lepší podpory roamingových scénářů v all-IP síti (EPS).

Řeší několik klíčových problémů: Za prvé poskytuje vyhrazený, zabezpečený vstupní bod pro aplikace služeb založených na poloze třetích stran, což umožňuje robustní autentizaci a vynucování politik ještě předtím, než jakýkoli požadavek na polohu vstoupí do jádra sítě. Za druhé centralizuje kontrolu soukromí proti profilu účastníka uloženému v HSS, což je klíčový požadavek regulatorních předpisů i důvěry spotřebitelů. Za třetí zjednodušuje logiku směrování v komplexních roamingových situacích tím, že existuje jasně definovaná „domovská“ entita, která rozhoduje, zda má požadavek předat do navštívené sítě. Tato architektura řeší omezení starších, monolitičtějších návrhů tím, že zlepšuje škálovatelnost, umožňuje podrobnější účtování za služby určování polohy a poskytuje čistší rozhraní pro vystavení síťových schopností, což se s růstem komerčních LBS stávalo stále důležitějším.

## Klíčové vlastnosti

- Slouží jako vstupní bod a brána pro požadavky na polohu od externích LCS Clientů.
- Provádí autentizaci a autorizaci žádajícího LCS Clienta.
- Vynucuje pravidla soukromí účastníka prostřednictvím komunikace s HSS.
- Směruje požadavky na polohu do příslušné sítě (domovské nebo navštívené).
- Formátuje a vrací odpovědi s polohou externímu klientovi.
- Komunikuje s dalšími uzly jádra sítě prostřednictvím standardizovaných rozhraní Lg a SLh.

## Související pojmy

- [H-GMLC – Home-Gateway Mobile Location Centre](/mobilnisite/slovnik/h-gmlc/)
- [V-GMLC – Visited-Gateway Mobile Location Centre](/mobilnisite/slovnik/v-gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [R-GMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-gmlc/)
