---
slug: "sage"
url: "/mobilnisite/slovnik/sage/"
type: "slovnik"
title: "SAGE – Security Algorithms Group of Experts"
date: 2025-01-01
abbr: "SAGE"
fullName: "Security Algorithms Group of Experts"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sage/"
summary: "Expertní skupina 3GPP odpovědná za návrh, vyhodnocení a standardizaci kryptografických algoritmů používaných pro zabezpečení systémů 3GPP. Vyvíjí základní algoritmy pro autentizaci, integritu a důvěrn"
---

SAGE je expertní skupina 3GPP odpovědná za návrh, vyhodnocení a standardizaci základních kryptografických algoritmů pro autentizaci, integritu a důvěrnost v systémech 3GPP.

## Popis

Security Algorithms Group of Experts (SAGE) je stálá pracovní skupina v rámci Evropského institutu pro telekomunikační standardy ([ETSI](/mobilnisite/slovnik/etsi/)), která vykonává klíčovou kryptografickou práci pro 3GPP. Není to síťová funkce ani protokol, ale orgán pro vývoj standardů složený z kryptografů a bezpečnostních expertů z členských společností. Primárním výstupem SAGE je specifikace kryptografických algoritmů, které tvoří základ bezpečnosti ve všech systémech 3GPP, od 3G (UMTS) přes 4G (LTE) až po 5G (NR).

SAGE funguje tak, že přijímá formální požadavky na návrh algoritmů od skupiny pro systémovou architekturu 3GPP (SA3), která je odpovědná za celkovou bezpečnostní architekturu. Tyto požadavky specifikují funkční potřeby (např. velikosti klíčů, výkonnostní omezení, odolnost vůči známým útokům) pro konkrétní algoritmus, jako je nový protokol pro autentizaci a dohodu klíčů ([AKA](/mobilnisite/slovnik/aka/)) nebo šifrovací algoritmus pro rozhraní přes vzduch. SAGE následně provádí vícefázový proces, který zahrnuje otevřenou výzvu pro kandidátní algoritmy z průmyslu a akademické sféry, důkladnou fázi vyhodnocení a testování a nakonec výběr a podrobnou specifikaci zvoleného algoritmu či algoritmů.

Práce skupiny pokrývá několik rodin algoritmů. Pro autentizaci a generování klíčů specifikovala SAGE sadu algoritmů Milenage (založenou na [AES](/mobilnisite/slovnik/aes/)) používanou v UMTS a LTE a později sadu algoritmů TUAK (založenou na Keccak/[SHA-3](/mobilnisite/slovnik/sha-3/)) jako alternativu. Pro důvěrnost a ochranu integrity na rozhraní přes vzduch vyvinula SAGE základní proudové šifry a režimy blokové šifry: blokovou šifru Kasumi pro 3G a proudovou šifru SNOW 3G a algoritmy založené na AES (128-EEA3/EIA3) pro LTE. Pro 5G specifikovala SAGE protokol 5G AKA a šifrovací a integritní algoritmy [NEA](/mobilnisite/slovnik/nea/)/[NIA](/mobilnisite/slovnik/nia/), což jsou profily stávajících algoritmů AES a SNOW 3G s novými specifickými režimy provozu.

Její role je naprosto zásadní. Algoritmy navržené SAGE jsou implementovány v každém uživatelském zařízení (UE) a v síťových prvcích, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Provádějí kritické funkce vzájemné autentizace mezi UE a sítí, generují relakční klíče používané pro šifrování a zajišťují integritu signalizačních zpráv. Bez práce SAGE by sítě 3GPP postrádaly standardizovanou, robustní a interoperabilní kryptografickou ochranu, což by je činilo zranitelnými vůči odposlechu, zosobnění a manipulaci s daty.

## K čemu slouží

SAGE byla zřízena, aby poskytla 3GPP specializovaný expertní zdroj pro návrh kryptografických algoritmů, což je úkol vyžadující hluboké specializované znalosti, které obvykle nemají obecní systémoví architekti. Před jejím zapojením měly rané buněčné systémy slabší, proprietární nebo nestandardizované kryptografické mechanismy. Vznik SAGE byl motivován potřebou silných, veřejně prověřených a standardizovaných bezpečnostních algoritmů, které by zajistily interoperabilitu mezi zařízeními různých výrobců při zachování vysoké úrovně ochrany proti vyvíjejícím se hrozbám.

Klíčový problém, který SAGE řeší, je problém 'černé skříňky' důvěry v síťovou bezpečnost. Prováděním otevřených hodnocení a standardizací algoritmů odstraňuje potřebu, aby každý operátor nebo výrobce vyvíjel vlastní (potenciálně slabou) kryptografii. Tím vytváří jednotnou, vysoce spolehlivou bezpečnostní základnu pro celý ekosystém. Řeší tak omezení předchozích přístupů, kde byla bezpečnost často až dodatečným zvážením nebo se spoléhala na tajné, neanalyzované návrhy, které mohly obsahovat fatální chyby objevené až po rozsáhlém nasazení.

Historicky práce SAGE začala vývojem proudových šifer A5/1 a A5/2 pro GSM (ačkoli se později ukázaly jako slabé), ale její formální, rigorózní proces byl ustálen pro 3G (UMTS). Vývoj bezpečnostní architektury UMTS přinesl nové výzvy vyžadující sadu algoritmů (funkce f1-f9) pro protokol AKA. Úspěšný návrh a specifikace šifry Kasumi a sady algoritmů Milenage ze strany SAGE nastavily vzor pro budoucí práci. Jejím trvalým účelem je neustále rozvíjet kryptografickou sadu nástrojů v reakci na rostoucí výpočetní výkon (který může prolomit starší algoritmy), nové kryptografické útoky a nové systémové požadavky od 5G a dále, jako je lehká kryptografie pro IoT nebo post-kvantová kryptografie pro dlouhodobou bezpečnost.

## Klíčové vlastnosti

- Návrh a specifikace 3GPP algoritmů pro autentizaci a dohodu klíčů (AKA) (Milenage, TUAK)
- Vývoj šifrovacích algoritmů pro rozhraní přes vzduch (např. 128-EEA1/EEA2/EEA3 pro LTE)
- Vývoj algoritmů ochrany integrity pro rozhraní přes vzduch (např. 128-EIA1/EIA2/EIA3 pro LTE)
- Správa otevřených procesů vyhodnocení a výběru nových kandidátních algoritmů
- Tvorba podrobných specifikací algoritmů a testovacích vektorů pro shodu implementace
- Průběžná údržba a vývoj portfolia algoritmů pro řešení nových hrozeb a požadavků

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [SAGE na 3GPP Explorer](https://3gpp-explorer.com/glossary/sage/)
