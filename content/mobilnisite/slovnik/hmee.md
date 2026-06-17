---
slug: "hmee"
url: "/mobilnisite/slovnik/hmee/"
type: "slovnik"
title: "HMEE – Hardware Mediated Execution Environment"
date: 2025-01-01
abbr: "HMEE"
fullName: "Hardware Mediated Execution Environment"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hmee/"
summary: "Bezpečnostní architektura využívající hardwarovou izolaci k ochraně kritického softwarového provádění před neoprávněnými zásahy. Zajišťuje integritu a důvěrnost citlivých operací, jako jsou kryptograf"
---

HMEE je bezpečnostní architektura využívající hardwarovou izolaci k ochraně kritického softwarového provádění před neoprávněnými zásahy, čímž zajišťuje integritu a důvěrnost citlivých operací v mobilních sítích.

## Popis

Hardware Mediated Execution Environment (HMEE) je bezpečnostní rámec definovaný 3GPP pro vytvoření důvěryhodného prováděcího prostředí (TEE), které je izolováno a chráněno hardwarovými mechanismy. Na rozdíl od čistě softwarových řešení se HMEE opírá o hardwarové funkce – jako jsou bezpečnostní rozšíření procesoru, jednotky ochrany paměti nebo vyhrazené bezpečnostní prvky – k vytvoření zabezpečené oblasti (secure enclave). Tato oblast chrání provádění citlivého kódu a dat před neoprávněným přístupem, a to i od privilegovaného softwaru, jako je operační systém nebo hypervizor. Architektura typicky zahrnuje proces zabezpečeného startu (secure boot), který ověřuje integritu firmwaru HMEE a zajišťuje jeho spuštění v známém dobrém stavu.

V rámci HMEE jsou prováděny kritické bezpečnostní funkce, včetně správy klíčů, kryptografických operací (např. šifrování, dešifrování, digitální podpisy) a autentizačních protokolů. Hardwarová mediace zajišťuje, že tyto funkce jsou odolné vůči manipulacím, a poskytuje kořen důvěry pro celý systém. HMEE komunikuje s dalšími síťovými komponentami prostřednictvím striktně definovaných rozhraní [API](/mobilnisite/slovnik/api/), která jsou navržena tak, aby zabránila úniku citlivých informací. Tato izolace je zásadní v prostředích s více nájemci (multi-tenant), jako je síťové dělení (network slicing) nebo cloud-nativní nasazení, kde více aplikací nebo síťových funkcí sdílí stejný fyzický hardware.

HMEE hraje klíčovou roli v zabezpečení 5G, zejména při ochraně infrastruktur virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a uzlů edge computingu. Podporuje zabezpečené poskytování služeb tím, že zajišťuje, že procesy kritické z hlediska bezpečnosti, jako jsou ty definované ve specifikacích 3GPP 33.127 a 33.848, nemohou být ohroženy softwarovými útoky. Díky využití hardwarově vynucených hranic HMEE zmírňuje hrozby, jako jsou útoky postranním kanálem (side-channel), vkládání kódu a neoprávněný přístup do paměti, čímž zvyšuje celkovou odolnost telekomunikačních sítí vůči vyvíjejícím se kybernetickým hrozbám.

## K čemu slouží

HMEE bylo zavedeno, aby řešilo rostoucí bezpečnostní výzvy v moderních telekomunikačních sítích, zejména s přechodem k virtualizovaným a cloud-nativním architekturám v 5G. Tradiční softwarové bezpečnostní mechanismy byly nedostatečné pro ochranu proti sofistikovaným útokům cílícím na hypervizory nebo operační systémy. HMEE poskytuje základ důvěry zakotvený v hardwaru, což zajišťuje, že kritické bezpečnostní funkce zůstanou v bezpečí, i když jsou jiné části systému ohroženy.

Motivace pro HMEE vychází z potřeby zvýšené izolace v prostředích s více dodavateli a službami, jako je síťové dělení (network slicing) a edge computing. Předchozí přístupy se silně spoléhaly na softwarovou izolaci, která mohla být zranitelná vůči exploitům. HMEE tyto rizika zmírňuje vynucováním oddělení na hardwarové úrovni, čímž podporuje regulatorní a compliance požadavky na ochranu dat a integritu sítě. Jeho vytvoření bylo hnací silou poptávky odvětví po robustních bezpečnostních rámcích, které mohou odolat pokročilým trvalým hrozbám (APT) a zároveň umožnit flexibilní nasazení sítí.

## Klíčové vlastnosti

- Hardwarově vynucená izolace pro zabezpečená prováděcí prostředí
- Podpora zabezpečeného startu (secure boot) a ověřování integrity
- Ochrana kryptografických klíčů a citlivých dat
- Odolnost vůči manipulacím a útokům postranním kanálem (side-channel)
- Rozhraní API pro zabezpečenou interakci s nedůvěryhodnými softwarovými komponentami
- Soulad s bezpečnostními specifikacemi 3GPP pro sítě 5G

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [HMEE na 3GPP Explorer](https://3gpp-explorer.com/glossary/hmee/)
