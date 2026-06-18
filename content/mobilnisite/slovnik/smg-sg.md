---
slug: "smg-sg"
url: "/mobilnisite/slovnik/smg-sg/"
type: "slovnik"
title: "SMG-SG – The ETSI TC SMG Security Group"
date: 2017-01-01
abbr: "SMG-SG"
fullName: "The ETSI TC SMG Security Group"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smg-sg/"
summary: "Skupina SMG Security Group (SMG-SG) byla specializovaná podskupina v rámci ETSI Special Mobile Group (SMG) zaměřená na bezpečnostní aspekty standardů GSM. Byla odpovědná za návrh a specifikaci kryptog"
---

SMG-SG je ETSI Special Mobile Group Security Group, podskupina odpovědná za návrh bezpečnostních standardů GSM, včetně autentizačních algoritmů A3/A8 a šifrovacího algoritmu A5.

## Popis

Skupina [SMG](/mobilnisite/slovnik/smg/) Security Group (SMG-SG) byla klíčovou pracovní entitou v organizační struktuře [ETSI](/mobilnisite/slovnik/etsi/) Special Mobile Group (SMG). Jejím výhradním mandátem bylo řešení všech bezpečnostních záležitostí systému GSM. Skupina fungovala s vysokým stupněm důvěrnosti kvůli citlivé povaze kryptografického návrhu. Hlavním technickým výstupem SMG-SG byla specifikace bezpečnostní architektury GSM a jejích klíčových kryptografických algoritmů. To zahrnovalo několik klíčových komponent. Za prvé definovala mechanismus autentizace a dohody klíče ([AKA](/mobilnisite/slovnik/aka/)). Ten využíval algoritmus [A3](/mobilnisite/slovnik/a3/) (pro autentizaci) a algoritmus [A8](/mobilnisite/slovnik/a8/) (pro generování šifrovacího klíče), které byly implementovány na modulu [SIM](/mobilnisite/slovnik/sim/) (Subscriber Identity Module) a v autentizačním centru (AuC) sítě. Sdílený tajný klíč (Ki) uložený na SIM a v AuC byl základem tohoto procesu. Za druhé skupina specifikovala rodinu proudových šifer A5 (např. [A5/1](/mobilnisite/slovnik/a5-1/), [A5/2](/mobilnisite/slovnik/a5-2/), A5/3) používaných k šifrování hlasového a datového provozu přes rozhraní rádiového přenosu mezi mobilní stanicí a základnovou přenosovou stanicí (BTS). Návrh a vyhodnocení těchto algoritmů prováděli bezpečnostní experti z členských organizací, často v uzavřených zasedáních. SMG-SG také pracovala na bezpečnostních protokolech signalizace a na celkových bezpečnostních cílech sítě, jako je utajení identity účastníka (pomocí dočasné identity mobilního účastníka - TMSI) a autentizace účastníka ze strany sítě. Její práce zajistila, že GSM jako první digitální celosvětový mobilní systém obsahovalo robustní bezpečnostní prvky, které představovaly významný pokrok oproti zranitelným analogovým systémům, které nahradilo.

## K čemu slouží

Vznik SMG-SG byl motivován základní potřebou zabezpečit novou digitální síť GSM proti řadě hrozeb, které bylo u analogových systémů buď nemožné, nebo obtížné řešit. Analogové mobilní signály byly snadno zachytitelné, což umožňovalo odposlech a klonování identit účastníků. Projekt GSM uznal, že pro získání důvěry uživatelů a přijetí operátory, zejména pro podnikové využití, je silná bezpečnost nezbytná. SMG-SG byla zformována, aby vyřešila tyto konkrétní problémy: zabránit neoprávněnému přístupu k síti (prostřednictvím silné vzájemné autentizace), chránit soukromí uživatelů šifrováním hlasových hovorů a dat na rádiové cestě a zabezpečit identitu účastníka. Odstranila omezení předchozích přístupů přechodem od bezpečnosti založené na utajení (jak bylo běžné u proprietárních analogových systémů) k standardizovanému bezpečnostnímu modelu založenému na algoritmech. Práci skupiny také ovlivňovaly vývozní kontroly kryptografie (jako např. z Dohody z Wassenaaru), což vedlo k vytvoření více verzí šifry A5 s různou silou. Cílem bylo navrhnout bezpečnostní systém, který byl pro svou dobu dostatečně silný, implementovatelný na omezeném hardwaru raných SIM karet a telefonů a přijatelný pro regulátory v různých zemích.

## Klíčové vlastnosti

- Vyčleněný orgán pro standardizaci bezpečnosti GSM v rámci ETSI SMG
- Specifikovala protokol GSM Authentication and Key Agreement (AKA) využívající algoritmy A3/A8
- Navrhla rodinu proudových šifer A5 pro šifrování přenosu vzduchem (A5/1, A5/2, A5/3)
- Spravovala důvěrné specifikace kryptografických algoritmů
- Definovala cíle bezpečnostní architektury: důvěrnost, autentizace a ochrana identity
- Řešila regulační omezení a omezení vývozních kontrol při návrhu šifer

## Související pojmy

- [SMG – Special Mobile Group](/mobilnisite/slovnik/smg/)

## Definující specifikace

- **TS 41.033** (Rel-14) — GSM Lawful Interception Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [SMG-SG na 3GPP Explorer](https://3gpp-explorer.com/glossary/smg-sg/)
