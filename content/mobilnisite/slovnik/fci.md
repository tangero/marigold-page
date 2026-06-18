---
slug: "fci"
url: "/mobilnisite/slovnik/fci/"
type: "slovnik"
title: "FCI – Furnish Charging Information"
date: 2025-01-01
abbr: "FCI"
fullName: "Furnish Charging Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fci/"
summary: "Furnish Charging Information (FCI) je operace protokolu založeného na Diameteru používaná v systému online účtování 3GPP (OCS). Jde o konkrétní příkaz na referenčním bodě Ro, kde OCS poskytuje autoriz"
---

FCI je příkaz protokolu Diameter na referenčním bodě Ro, kde systém online účtování (OCS) poskytuje autorizované účtovací informace, jako přidělené servisní jednotky a ratingová data, síťovému elementu žádajícímu o kvótu pro účastnickou relaci.

## Popis

Furnish Charging Information (FCI) je klíčový příkaz Diameter aplikace v architektuře systému online účtování 3GPP ([OCS](/mobilnisite/slovnik/ocs/)), definovaný pro referenční bod Ro (mezi OCS a funkcí spouštění účtování v síti – [CTF](/mobilnisite/slovnik/ctf/)). Není to kanál ani samostatný protokol, ale konkrétní transakce typu požadavek-odpověď (Diameter Command Code 272). Hlavní funkcí příkazu FCI je, aby OCS doručil autorizované účtovací informace síťovému elementu, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)), který funguje jako funkce spouštění účtování (CTF). K této transakci dochází poté, co CTF odeslalo OCS žádost o řízení kreditu ([CCR](/mobilnisite/slovnik/ccr/)) pro získání kvóty za účastníkovo využití služby.

Příkaz FCI, odesílaný jako odpověď na řízení kreditu ([CCA](/mobilnisite/slovnik/cca/)), nese rozhodnutí OCS ve formě specifických atribut-hodnotových párů ([AVP](/mobilnisite/slovnik/avp/)). Tyto AVP tvoří ‚poskytované‘ informace a zahrnují přidělené servisní jednotky (např. objem dat v bajtech, délku hovoru v sekundách nebo peněžní kredit), přidružené identifikátory ratingových skupin, dobu platnosti kvóty a indikaci poslední jednotky (signalizující poslední přidělenou kvótu). Klíčově může FCI také obsahovat AVP s informacemi o ceně, které CTF poskytují peněžní náklady na přidělené servisní jednotky. To umožňuje CTF potenciálně informovat účastníka v reálném čase o účtování, což je funkce známá jako Advice of Charge (AoC). OCS tyto informace určuje provedením ratingu a správy zůstatku v reálném čase na základě účtu účastníka a požadované služby.

Architektonicky je FCI základní součástí funkcí účtování na základě událostí (EBC) a účtování na základě relací (SBC) v rámci OCS. Umožňuje proces ‚autorizace kreditu‘. Když CTF obdrží příkaz FCI, aplikuje přidělenou kvótu na uživatelskou relaci, čímž umožní pokračování služby. Následně monitoruje využití prostředků v reálném čase. Když je kvóta vyčerpána nebo relace skončí, CTF odešle novou CCR, aby nahlásilo použité jednotky, a pokud relace pokračuje, spustí další výměnu FCI/CCA pro získání nové kvóty. Tento cyklus CCR (žádost) a CCA s FCI (odpověď) tvoří základ reálného času, předplaceného a konvergentního účtování v sítích 3GPP a zajišťuje, že služby jsou doručovány pouze tehdy, má-li účastník dostatečný kredit.

## K čemu slouží

FCI bylo vytvořeno pro podporu evoluce od tradičního offline (postpaid) účtování k online účtování v reálném čase, což je zásadní pro předplacené služby a kontrolu výdajů. Před online účtováním sítě nejprve poskytovaly služby a poplatky vypočítávaly až následně (offline), což s sebou neslo riziko špatných pohledávek a neumožňovalo kontrolu kreditu v reálném čase. Účelem příkazu FCI je umožnit bezpečný, standardizovaný a časově okamžitý dialog, ve kterém může síťový účtovací systém (OCS) autorizovat a měřit poskytování služeb okamžitě.

Řeší problém, jak integrovat centralizovaný, inteligentní účtovací systém s různorodými síťovými elementy, které služby skutečně poskytují (hlasové hovory, datové relace, SMS, IMS služby). Příkaz FCI v rámci protokolu Diameter poskytuje konkrétní mechanismus, kterým OCS ‚poskytuje‘ nebo zásobuje CTF přesnými podmínkami autorizace služby: kolik služby (kvóta) je povoleno a za jakou cenu. Tím odstraňuje omezení neinteraktivního účtování tím, že umožňuje okamžité kontroly kreditu, odečty z předplaceného zůstatku a vynucování kvót.

Jeho vytvoření bylo motivováno komerční potřebou flexibilních, časově okamžitých účtovacích modelů pro vytváření nových zdrojů příjmů, zejména pro předplacené mobilní služby, které v mnoha trzích dominují. Operace protokolu FCI umožňuje operátorům implementovat nejen jednoduché předplacené služby, ale také hybridní účty, propagační nabídky a limity výdajů v reálném čase. Standardizací tohoto příkazu v rozhraní Ro zajistilo 3GPP interoperabilitu mezi platformami OCS od různých dodavatelů a množstvím síťových elementů generujících účtovací události, čímž vytvořilo páteř moderní telekomunikační monetizace.

## Klíčové vlastnosti

- Definován jako Diameter Command Code 272 pro zprávu Credit-Control-Answer (CCA) na referenčním bodě Ro.
- Přenáší přidělené servisní jednotky (objem, čas, peníze) z OCS do funkce spouštění účtování (CTF).
- Obsahuje AVP pro ratingovou skupinu a cenové informace, což umožňuje rating v reálném čase a funkci Advice of Charge (AoC).
- Podporuje scénáře online účtování jak na základě relací, tak na základě událostí.
- Spouští v CTF aplikaci kvóty a umožnění poskytnutí služby účastníkovi.
- Ústřední pro smyčku autorizace kreditu mezi síťovými elementy a systémem online účtování (OCS).

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [FCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fci/)
