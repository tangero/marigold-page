---
slug: "pspl"
url: "/mobilnisite/slovnik/pspl/"
type: "slovnik"
title: "PSPL – Preferred Service Providers List"
date: 2025-01-01
abbr: "PSPL"
fullName: "Preferred Service Providers List"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pspl/"
summary: "Seznam preferovaných poskytovatelů síťových služeb uložený na UICC (SIM kartě) nebo v paměti zařízení. Řídí proces výběru sítě zařízením, zejména pro přístup mimo 3GPP (jako je WLAN), tím, že upřednos"
---

PSPL je seznam preferovaných poskytovatelů síťových služeb uložený na SIM kartě nebo v zařízení, který řídí výběr sítě, zejména pro přístup mimo 3GPP (např. WLAN), tím, že upřednostňuje konkrétní sítě operátorů.

## Popis

Preferred Service Providers List (PSPL) je objekt správy definovaný ve specifikacích 3GPP, který obsahuje uspořádaný seznam identifikátorů poskytovatelů služeb. Používá jej uživatelské zařízení (UE) k řízení svého výběru sítě a postupů připojení, zejména při přístupu k sítím prostřednictvím technologií mimo 3GPP, jako je bezdrátová lokální síť ([WLAN](/mobilnisite/slovnik/wlan/)). PSPL je typicky zřizován na univerzální integrované obvodové kartě (UICC) mobilním síťovým operátorem ([MNO](/mobilnisite/slovnik/mno/)), ale může být také nakonfigurován v paměti zařízení prostřednictvím protokolů správy zařízení, jako je [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/).

Hlavní operační role PSPL vstupuje do hry během operací funkce pro vyhledávání a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo obecnější logiky výběru sítě. ANDSF je funkce jádra sítě, která poskytuje UE politiky pro vyhledávání a výběr mezi přístupovými sítěmi 3GPP a mimo 3GPP. PSPL slouží jako klíčový vstup pro tyto politiky. Když UE skenuje dostupné WLAN sítě, může porovnat nalezené identifikátory sady služeb ([SSID](/mobilnisite/slovnik/ssid/)) nebo jiné identifikátory se záznamy ve svém PSPL. Seznam je uspořádán podle priority. UE se pokusí připojit k nejvyšší prioritě dostupného poskytovatele služeb v seznamu, což usnadňuje plynulé připojení k partnerským nebo preferovaným hotspotům.

Záznamy v seznamu jsou definovány pomocí formátu identifikátoru poskytovatele služeb ([SPID](/mobilnisite/slovnik/spid/)). Správa PSPL – jeho vytváření, aktualizace a mazání – je prováděna prostřednictvím standardizovaných rozhraní a protokolů. Pro úložiště na bázi UICC je součástí souborového systému na [SIM](/mobilnisite/slovnik/sim/) kartě. Pro správu na straně zařízení může být PSPL doručen prostřednictvím OMA DM nebo potenciálně samotným serverem ANDSF jako součást kontejneru politik. Použití PSPL zlepšuje uživatelský zážitek automatizací připojení k důvěryhodným a potenciálně zpoplatnitelným WLAN sítím, podporuje strategie odlehčování provozu a umožňuje operátorem řízené připojení v heterogenních síťových prostředích.

## K čemu slouží

PSPL byl zaveden, aby řešil rostoucí složitost výběru sítě v heterogenních bezdrátových prostředích. Jak se chytré telefony staly všudypřítomnými, uživatelé získali přístup k více typům sítí: mobilním (3GPP) a Wi-Fi (mimo 3GPP). Ruční výběr Wi-Fi sítě z dlouhého seznamu byl pro uživatele zdlouhavý a pro operátory, kteří chtěli směrovat provoz na preferované nebo partnerské sítě, neefektivní. PSPL poskytuje automatizovaný, operátorem řízený mechanismus pro stanovení priority výběru sítě.

Jeho vytvoření bylo motivováno potřebou podporovat plynulou mobilitu a odlehčování provozu. Pro operátory je odlehčení datového provozu na WLAN cenným nástrojem pro správu kapacity. PSPL umožňuje operátorovi zajistit, aby se zařízení účastníka automaticky připojilo k vlastním značkovým Wi-Fi hotspotům operátora nebo k síti partnera, nikoli k neznámé nebo méně preferované veřejné Wi-Fi. Toto zlepšuje zabezpečení (směrováním na důvěryhodné sítě), umožňuje plynulé ověřování (prostřednictvím přihlašovacích údajů na bázi SIM, jako je EAP-AKA) a podporuje obchodní modely, jako jsou balíčkové služby mobilní a Wi-Fi sítě. Vyřešil omezení čistě na základě síly signálu, čímž do logiky připojení zařízení zavedl řízený prioritní schéma založené na politikách a zaměřené na operátora.

## Klíčové vlastnosti

- Uspořádaný seznam identifikátorů preferovaných poskytovatelů služeb (SPID)
- Uložen na UICC (SIM) nebo v paměti zařízení
- Slouží k řízení výběru sítě, primárně pro přístup mimo 3GPP jako je WLAN
- Integruje se s politikami ANDSF pro inteligentní výběr přístupu
- Umožňuje automatické připojení k operátorem preferovaným nebo partnerským sítím
- Podporuje strategie operátora pro směrování a odlehčování provozu

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [SPID – Subscriber Profile ID for RAT/Frequency Priority](/mobilnisite/slovnik/spid/)
- [WLAN – Wireless Local Area Network](/mobilnisite/slovnik/wlan/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [PSPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/pspl/)
