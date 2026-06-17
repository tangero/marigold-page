---
slug: "mv"
url: "/mobilnisite/slovnik/mv/"
type: "slovnik"
title: "MV – Membership Verification"
date: 2025-01-01
abbr: "MV"
fullName: "Membership Verification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mv/"
summary: "Membership Verification (MV, ověření členství) je služba 3GPP, která umožňuje uživateli prokázat svou příslušnost ke skupině ověřovateli bez odhalení své identity. Je klíčová pro řízení přístupu s och"
---

MV je služba 3GPP, která umožňuje uživateli prokázat svou příslušnost ke skupině ověřovateli bez odhalení své identity; používá se pro řízení přístupu s ochranou soukromí.

## Popis

Membership Verification (MV, ověření členství) je standardizovaná služba definovaná v rámci architektury 3GPP, která umožňuje anonymní, avšak autentizovaný skupinový přístup. Základní architektura zahrnuje tři primární entity: uživatele (prokazovatele), ověřovatele (poskytovatele služby) a důvěryhodnou třetí stranu, kterou je často mobilní operátor ([MNO](/mobilnisite/slovnik/mno/)) nebo specializovaný vystavovatel přihlašovacích údajů. Uživatel vlastní přihlašovací údaj vystavené vystavovatelem, které potvrzují jeho příslušnost ke konkrétní skupině (např. odběratelé prémiové služby, členové firemního tarifu nebo osoby určité věkové kategorie). Tyto přihlašovací údaje jsou kryptograficky svázány s uživatelovým předplatným, ale jsou navrženy tak, aby neumožňovaly propojení mezi různými ověřovacími relacemi.

Protokol funguje tak, že uživateli umožňuje vygenerovat důkaz s nulovým rozšířením znalostí nebo podobný kryptografický token odvozený z jeho přihlašovacích údajů členství. Při přístupu ke službě vyžadující skupinové ověření předloží uživatel tento důkaz ověřovateli. Ověřovatel může kryptograficky zkontrolovat platnost důkazu vůči veřejnému skupinovému podpisu nebo certifikátu poskytnutému důvěryhodným vystavovatelem. Klíčové je, že důkaz odhalí pouze fakt členství a případně některé autorizované atributy (jako 'starší 18 let'), aniž by prozradil konkrétní identitu uživatele (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)) nebo umožnil ověřovateli spojit více přístupů od stejného uživatele. Role MNO je klíčová při vystavování, správě a případném odvolávání těchto anonymních přihlašovacích údajů, neboť využívá svou důvěryhodnou pozici v síti.

Úloha MV v síti spočívá v oddělení přístupu ke službám od odhalení identity, přičemž funguje jako vrstva zvyšující soukromí nad základními autentizačními mechanismy, jako je 5G [AKA](/mobilnisite/slovnik/aka/). Integruje se do bezpečnostní architektury sítě a využívá schopnosti domovské sítě vystavovat přihlašovací údaje. Mezi klíčové technické komponenty patří struktura přihlašovacích údajů MV, algoritmy pro generování a ověřování důkazů a protokoly pro vystavování a obnovu přihlašovacích údajů. To umožňuje škálovatelný a na ochranu soukromí vyhovující přístup ke skupinovým službám, aniž by poskytovatelé služeb museli přímo spravovat identity uživatelů.

## K čemu slouží

MV byla vytvořena jako odpověď na rostoucí poptávku po ochraně soukromí v digitálních službách, kterou podnítily předpisy jako GDPR. Tradiční řízení přístupu často vyžaduje, aby se uživatelé identifikovali (např. přihlášením), což nutí ke kompromisu mezi přístupem ke službě a soukromím. U mnoha služeb potřebuje poskytovatel vědět pouze to, zda uživatel patří do povolené skupiny, nikoli jeho přesnou identitu. MV to řeší tím, že poskytuje technický standard pro systémy anonymních přihlašovacích údajů v mobilních sítích.

Historicky se používala ad-hoc řešení nebo spoléhání se na plnou autentizaci, což buď narušovalo soukromí, nebo bylo neefektivní. MV využívá roli mobilního operátora jako důvěryhodného poskytovatele identity k vystavování ověřených, avšak anonymizovaných potvrzení o členství. To umožňuje nové obchodní modely, jako je anonymní přístup k lokalizačním propagačním akcím, obsah s věkovým omezením bez předkládání dokladu totožnosti nebo zabezpečený přístup k firemním zdrojům bez vystavení údajů zaměstnance poskytovateli aplikace. Řeší omezení předchozích přístupů standardizací kryptograficky robustní, interoperabilní a síťově integrované metody pro ověřování s ochranou soukromí.

## Klíčové vlastnosti

- Umožňuje ověření skupinového členství bez odhalení jedinečné identity uživatele
- Podporuje selektivní zveřejnění autorizovaných atributů (např. věková skupina, úroveň předplatného)
- Poskytuje nepropojitelnost mezi různými ověřovacími relacemi, aby zabránila sledování uživatele
- Využívá mobilního operátora jako důvěryhodného vystavovatele přihlašovacích údajů
- Integruje se s bezpečnostní architekturou 3GPP a autentizačními rámci
- Zahrnuje mechanismy pro odvolání přihlašovacích údajů pro správu změn skupinového členství

## Související pojmy

- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 37.803** (Rel-11) — H(e)NB Mobility Enhancements Study

---

📖 **Anglický originál a plná specifikace:** [MV na 3GPP Explorer](https://3gpp-explorer.com/glossary/mv/)
