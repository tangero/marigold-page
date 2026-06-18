---
slug: "gpi"
url: "/mobilnisite/slovnik/gpi/"
type: "slovnik"
title: "GPI – GBA Push Information"
date: 2025-01-01
abbr: "GPI"
fullName: "GBA Push Information"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gpi/"
summary: "GBA Push Information (GPI) je bezpečnostní mechanismus, který umožňuje síťovému aplikačnímu serveru bezpečně 'poslat' (push) bootstrapové informace uživatelskému zařízení (UE). Je součástí architektur"
---

GPI je bezpečnostní mechanismus architektury GBA, který umožňuje síťovému aplikačnímu serveru bezpečně zaslat bootstrapové informace uživatelskému zařízení (UE) pro zahájení nastavení komunikace.

## Popis

[GBA](/mobilnisite/slovnik/gba/) Push Information (GPI) je součást architektury 3GPP Generic Bootstrapping Architecture (GBA), která poskytuje standardizovanou metodu pro vzájemné ověření a dohodu klíčů mezi uživatelským zařízením (UE) a síťovou aplikační funkcí ([NAF](/mobilnisite/slovnik/naf/)). Zatímco standardní GBA spoléhá na to, že UE zahájí bootstrapový proces, GPI umožňuje 'push' model. V tomto modelu může NAF (např. server poskytovatele služeb) proaktivně odeslat základní bootstrapové informace uživatelskému zařízení, což tomuto zařízení následně umožní navázat zabezpečené spojení s danou NAF. Tyto informace jsou obsaženy v GPI zprávě, která je sama o sobě zabezpečeným objektem.

Z architektonického hlediska se GPI týká několika klíčových entit definovaných v GBA: UE, funkce bootstrapového serveru ([BSF](/mobilnisite/slovnik/bsf/)), NAF a domácího serveru účastníka ([HSS](/mobilnisite/slovnik/hss/)). Proces začíná, když NAF rozhodne, že potřebuje zaslat informace konkrétnímu UE. NAF požádá BSF o GPI. BSF, která má vztah důvěry s HSS, GPI vygeneruje. Tato GPI obsahuje kritická data, jako je identifikátor bootstrapové transakce ([B-TID](/mobilnisite/slovnik/b-tid/)), identitu NAF, informace o životnosti klíče a případně další parametry. Tato GPI je klíčově chráněna kryptograficky pomocí klíčů odvozených z dlouhodobých přihlašovacích údajů účastníka uložených v HSS, což zajišťuje její integritu a autenticitu. BSF odešle GPI NAF, která ji následně doručí uživatelskému zařízení prostřednictvím push kanálu, kterým může být IP-based push mechanismus jako [SIP](/mobilnisite/slovnik/sip/) Push nebo přenos přes [SMS](/mobilnisite/slovnik/sms/).

Po přijetí GPI ji uživatelské zařízení zpracuje. UE může ověřit autenticitu GPI, protože může odvodit stejné kryptografické klíče z vlastního identifikačního modulu ([USIM](/mobilnisite/slovnik/usim/)/ISIM) a parametrů obsažených v GPI. Po ověření UE extrahuje B-TID a další informace. Uživatelské zařízení pak může kontaktovat BSF pomocí tohoto B-TID a provést standardní GBA bootstrapový běh, jehož výsledkem je vytvoření sdílených relaních klíčů (Ks_NAF) určených speciálně pro použití s danou NAF. Nakonec uživatelské zařízení naváže s NAF zabezpečené spojení (např. pomocí TLS) za použití těchto klíčů. Tento mechanismus umožňuje službám, jako jsou bezdrátové aktualizace firmwaru (FOTA), aktivace služeb instant messagingu nebo systémy nouzového varování, aby bezpečně zahájily kontakt se zařízením, které s daným servisním serverem dříve nekomunikovalo.

## K čemu slouží

GPI bylo vytvořeno, aby odstranilo omezení původního modelu GBA, který byl čistě 'pull'-based (tažený), a vyžadoval, aby uživatelské zařízení vždy iniciovalo kontakt s BSF. Mnoho nově vznikajících mobilních služeb je však iniciováno serverem (push služby). Například poskytovatel služby může potřebovat odeslat konfigurační aktualizaci nebo výstrahu zařízení. Bez předem vytvořeného bezpečnostního kontextu je zahájení takové komunikace bezpečným způsobem obtížné. GPI tento problém řeší tím, že umožňuje serveru bezpečně zaslat uživatelskému zařízení úvodní bootstrapovou 'pozvánku'.

Historicky, před standardizovanými push bezpečnostními mechanismy, služby používaly méně bezpečné metody, jako je prostý SMS pro aktivaci, nebo spoléhaly na předem zřízené klíče, které bylo obtížné spravovat ve velkém měřítku. GPI, zavedené ve 3GPP Release 8 spolu s vylepšeními GBA, využilo stávající robustní zabezpečení infrastruktury GBA (zakořeněné v USIM), aby umožnilo bezpečné služby iniciované serverem. Vyplnilo kritickou mezeru v ekosystému zpřístupňování služeb, což umožnilo bezpečné, škálovatelné a standardizované doručování služeb založených na push mechanismu bez nutnosti úprav SIM karty uživatelského zařízení pro každou novou službu.

## Klíčové vlastnosti

- Umožňuje push model pro bootstrapování v rámci architektury Generic Bootstrapping Architecture (GBA)
- Umožňuje síťové aplikační funkci (NAF) zahájit zabezpečenou komunikaci s uživatelským zařízením (UE)
- GPI zpráva obsahuje identifikátor bootstrapové transakce (B-TID) a identitu NAF
- Kryptograficky chráněno klíči odvozenými z přihlašovacích údajů USIM/ISIM účastníka
- Doručeno uživatelskému zařízení prostřednictvím push mechanismů, jako je SIP Push nebo SMS
- Uživatelské zařízení použije obsah GPI k provedení následného standardního GBA bootstrapového běhu s BSF

## Související pojmy

- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [NAF – Network Application Function](/mobilnisite/slovnik/naf/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 33.224** (Rel-19) — Generic Push Layer (GPL) Specification
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification

---

📖 **Anglický originál a plná specifikace:** [GPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpi/)
