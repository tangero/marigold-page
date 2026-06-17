---
slug: "jcre"
url: "/mobilnisite/slovnik/jcre/"
type: "slovnik"
title: "JCRE – Java Card™ Run Time Environment"
date: 2025-01-01
abbr: "JCRE"
fullName: "Java Card™ Run Time Environment"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jcre/"
summary: "Java Card Run Time Environment (JCRE) je zabezpečená, standardizovaná softwarová platforma, která umožňuje aplikacím založeným na Javě (applety) běžet na čipových kartách a vestavěných bezpečnostních"
---

JCRE je zabezpečená, standardizovaná softwarová platforma Java Card Run Time Environment, která umožňuje aplikacím (appletům) založeným na Javě běžet na čipových kartách a vestavěných bezpečnostních prvcích, jako jsou např. UICC v mobilních zařízeních.

## Popis

Java Card Run Time Environment (JCRE) je podmnožinou platformy Java speciálně navržená pro hardwarová zabezpečená zařízení s omezenými prostředky, jako jsou čipové karty, UICC (Universal Integrated Circuit Card) a vestavěné bezpečnostní prvky (eSE). Podle specifikací 3GPP, jako je TS 51.013, a s odkazem ve slovníku TS 21.905, tvoří JCRE základní softwarovou vrstvu, která řídí provádění applety Java Card. Její architektura je rozdělena do zabezpečeného, izolovaného prostředí na čipu karty. JCRE se skládá z několika klíčových komponent: Java Card Virtual Machine (JCVM), která interpretuje bajtkód pro applety; Java Card Framework, který poskytuje sadu rozhraní [API](/mobilnisite/slovnik/api/) (např. javacard.framework, javacard.security) pro přístup applety ke službám karty, jako jsou kryptografické operace, komunikace [APDU](/mobilnisite/slovnik/apdu/) (Application Protocol Data Unit) a trvalé ukládání objektů; a systémových tříd JCRE, které zajišťují základní služby, jako je instalace, registrace, výběr applety a izolace mezi applety založená na firewallu. Princip činnosti: Když mobilní zařízení nebo terminál odešle příkaz APDU na UICC, komunikační systém JCRE jej přijme, identifikuje cílový applet (prostřednictvím jeho identifikátoru aplikace - [AID](/mobilnisite/slovnik/aid/)) a předá příkaz metodě process tohoto applety v jeho chráněném kontextu. Applet je prováděn za použití JCVM, může volat metody rozhraní API JCRE pro provádění kryptografických operací nebo správu dat a vrátí odpověď APDU. JCRE vynucuje striktní bezpečnostní hranice prostřednictvím svého firewallu pro applety, čímž zabraňuje neoprávněnému přístupu mezi applety, pokud není výslovně povolen prostřednictvím sdílených rozhraní. Jeho role v síti je zásadní pro mobilní zabezpečení, protože hostuje aplikaci USIM, která provádí autentizaci účastníka (pomocí algoritmů MILENAGE), ukládá kryptografické klíče a umožňuje zabezpečené služby, jako je mobilní bankovnictví, dopravní odbavení a správa identity zařízení.

## K čemu slouží

JCRE bylo vytvořeno pro uspokojení potřeby standardizované, víceaplikované platformy na čipových kartách, která překonává omezení proprietárních, monolitických operačních systémů karet. Před technologií Java Card každý vydavatel nebo výrobce karet vyvíjel vlastní software, což ztěžovalo nasazení, aktualizaci nebo správu více aplikací od různých dodavatelů na jedné kartě. Technologie Java Card s JCRE jako svým výkonovým prostředím zavedla přenositelnost applety na kartě typu „napiš jednou, spusť kdekoli“, což významně snížilo dobu a náklady na vývoj. V kontextu 3GPP bylo její přijetí pro UICC motivováno snahou o flexibilní, budoucím vývojům odolávající platformu pro USIM, která umožňuje, aby se SIM karta vyvinula mimo základní autentizaci a mohla hostovat nadstandardní služby (např. platby NFC, identitu). Vyřešila problém izolovaného a nezabezpečeného vývoje aplikací tím, že poskytla dobře definovaný, zabezpečený izolovaný prostor pro provádění (sandbox) se standardizovanými rozhraními [API](/mobilnisite/slovnik/api/), což zajišťuje, že applety od různých poskytovatelů mohou koexistovat bez narušení zabezpečení nebo stability karty. Historicky její zavedení souviselo s celoprůmyslovým přesunem k otevřeným standardům a programovatelnému hardwaru, což umožnilo mobilním síťovým operátorům personalizovat karty službami po jejich vydání a podpořilo ekosystém vývojářů zabezpečených applety třetích stran.

## Klíčové vlastnosti

- Zabezpečené, izolované výkonové prostředí s firewallem pro applety
- Standardizovaná rozhraní API Java Card pro kryptografii, vstup/výstup a trvalé ukládání
- Interpretace bajtkódu prostřednictvím Java Card Virtual Machine (JCVM)
- Správa životního cyklu applety (instalace, vytvoření instance, výběr, odstranění)
- Podpora zabezpečené správy karty v souladu se standardem GlobalPlatform
- Komunikace mezi applety prostřednictvím objektů se sdíleným rozhraním

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [JCRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/jcre/)
