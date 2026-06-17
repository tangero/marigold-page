---
slug: "foss"
url: "/mobilnisite/slovnik/foss/"
type: "slovnik"
title: "FOSS – Free and Open Source Software"
date: 2026-01-01
abbr: "FOSS"
fullName: "Free and Open Source Software"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/foss/"
summary: "FOSS označuje software, jehož zdrojový kód je veřejně dostupný a lze jej volně používat, upravovat a distribuovat. V rámci 3GPP je jeho použití řízeno bezpečnostními politikami, které zajišťují integr"
---

FOSS je typ softwaru, jehož veřejně dostupný zdrojový kód lze volně používat, upravovat a distribuovat; jeho použití v rámci 3GPP je řízeno bezpečnostními politikami za účelem ochrany integrity sítě.

## Popis

Free and Open Source Software (FOSS) v kontextu 3GPP není konkrétní protokol nebo síťový prvek, ale kategorie softwaru, jejíž licenční a distribuční model je řešen z bezpečnostní a řídicí perspektivy. Specifikace 3GPP, zejména v řadě 33 (Bezpečnost), poskytují pokyny a požadavky pro používání FOSS v síťových funkcích a produktech. To zahrnuje zavedení procesů bezpečnostního zajištění pro řízení rizik spojených s integrací externě vyvinutého, veřejně dostupného kódu do kritických telekomunikačních systémů.

Architektonické hledisko pro FOSS je integrováno do širšího rámce specifikace bezpečnostního zajištění (SCAS). Když dodavatel síťové funkce zahrne FOSS komponenty, musí celý produkt včetně těchto komponent podrobit bezpečnostnímu hodnocení. Otevřená povaha zdrojového kódu znamená, že potenciální zranitelnosti jsou veřejně dohledatelné, což vyžaduje robustní procesy správy zranitelností a nasazování záplat. Provozovatel sítě nebo dodavatel je odpovědný za vedení soupisu softwarových komponent (SBOM) ke sledování všech závislostí na FOSS.

Jeho role v síti je základní, ale nepřímá, protože FOSS komponenty mohou být součástí prakticky jakéhokoli síťového softwaru, od funkcí jádra sítě, jako je [AMF](/mobilnisite/slovnik/amf/) nebo [SMF](/mobilnisite/slovnik/smf/), přes platformy pro správu a orchestraci ([MANO](/mobilnisite/slovnik/mano/)) až po software pro rádiový přístupový síť. Bezpečnostní specifikace 3GPP ukládají, že použití FOSS nesmí ohrozit celkové bezpečnostní cíle důvěrnosti, integrity a dostupnosti. To vyžaduje pečlivou integraci, nepřetržité sledování bezpečnostních oznámení pro používané FOSS knihovny a schopnost rychle nasazovat aktualizace nebo zmírňující opatření k řešení nově objevených chyb.

## K čemu slouží

Formální zpracování FOSS ve specifikacích 3GPP bylo motivováno jeho rozšířeným a rostoucím přijetím v telekomunikačním průmyslu. Používání FOSS může urychlit vývoj, snížit náklady a podpořit inovace využitím projektů řízených komunitou. To však přineslo nové bezpečnostní výzvy pro provozovatele sítí a regulátory zvyklé na proprietární softwarové zásobníky řízené dodavatelem, kde celý kódový základ podléhal důvěrným bezpečnostním hodnocením.

Předchozí přístupy často postrádaly formální politiky pro open-source software, což mohlo vést k neřízeným bezpečnostním rizikům, problémům s dodržováním licencí a nepředvídatelným životním cyklům podpory. Účelem definování pokynů pro FOSS v 3GPP bylo vytvořit standardizovaný bezpečnostní rámec, který umožní průmyslu těžit z open-source inovací, a zároveň zajistit, aby splňoval vysoké požadavky na zajištění a spolehlivost sítí operátorské třídy. Řeší problém, jak zachovat bezpečnostní odpovědnost v dodavatelském řetězci, který zahrnuje softwarové komponenty s různým autorstvím a mírou transparentnosti.

## Klíčové vlastnosti

- Řízeno specifikacemi bezpečnostního zajištění 3GPP (např. TS 33.117)
- Vyžaduje bezpečnostní hodnocení konečného produktu včetně FOSS komponent
- Ukládá procesy správy zranitelností pro veřejně oznámené chyby
- Vyžaduje vedení soupisu softwarových komponent (SBOM)
- Musí dodržovat příslušné open-source licence
- Podporuje integraci bezpečnostních záplat bez ohrožení stability sítě

## Definující specifikace

- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [FOSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/foss/)
