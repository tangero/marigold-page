---
slug: "waf"
url: "/mobilnisite/slovnik/waf/"
type: "slovnik"
title: "WAF – WebRTC Authentication Function"
date: 2025-01-01
abbr: "WAF"
fullName: "WebRTC Authentication Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/waf/"
summary: "WebRTC Authentication Function (WAF) je bezpečnostní entita v rámci IP Multimedia Subsystem (IMS), která poskytuje služby autentizace a dohodnutí klíčů pro klienty založené na WebRTC. Umožňuje zabezpe"
---

WAF je bezpečnostní entita v rámci IMS, která poskytuje služby autentizace a dohodnutí klíčů pro klienty založené na WebRTC, aby umožnila zabezpečený přístup k IMS službám.

## Popis

WebRTC Authentication Function (WAF) je klíčová bezpečnostní komponenta definovaná 3GPP pro integraci klientů Web Real-Time Communication (WebRTC) do sítě IP Multimedia Subsystem (IMS). Funguje jako specializovaný proxy server pro autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)), který usnadňuje proceduru autentizace s podporou [GBA](/mobilnisite/slovnik/gba/) pro klienty WebRTC, kterým chybí tradiční karta [USIM](/mobilnisite/slovnik/usim/). Primární role WAF je působit jako důvěryhodný zprostředkovatel mezi klientem WebRTC (např. prohlížečem) a funkcí 3GPP Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)). Autentizační tok začíná, když se klient WebRTC, který žádá o přístup k IMS službám jako hlas nebo video přes LTE (VoLTE/ViLTE), obrátí na WAF. WAF jménem klienta zahájí proceduru GBA (Generic Bootstrapping Architecture) bootstrappingu s BSF. Používá dlouhodobé přihlašovací údaje uživatele (spravované BSF a [HSS](/mobilnisite/slovnik/hss/)) k vytvoření sdíleného tajemství. WAF následně vygeneruje krátkodobý autentizační token (tzv. 'WebRTC Token') a odpovídající klíč, které bezpečně doručí klientovi, typicky přes [TLS](/mobilnisite/slovnik/tls/) chráněné spojení. Klient tento token a klíč použije k přímé autentizaci vůči jádru IMS, konkrétně funkci Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), pomocí protokolu IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) upraveného pro přístup založený na tokenech. WAF je specifikována v několika technických specifikacích (TS): 24.371 definuje celkovou architekturu a procedury, 29.228/29.229 podrobně popisují rozhraní založená na Diameter (Mw a Mx) mezi WAF, BSF a HSS a specifikace řady 33.1xx pokrývají bezpečnostní mechanismy a analýzy hrozeb. Tato architektura umožňuje webové aplikaci využít identitu uživatele z mobilní sítě pro silnou autentizaci, aniž by byly přihlašovací údaje jádra sítě vystaveny prostředí prohlížeče.

## K čemu slouží

WAF byla vytvořena, aby vyřešila zásadní bezpečnostní a integrační výzvu umožnění přístupu aplikací WebRTC ve standardních webových prohlížečích k zabezpečeným, operátorsky kvalitním IMS službám. Před jejím zavedením byly IMS služby výhradně přístupné nativním klientům v UE vybaveným USIM, které mohly provést standardní IMS AKA autentizaci. Vzestup WebRTC představoval pro operátory příležitost nabízet komunikační služby přímo z webové stránky, ale izolované prostředí prohlížeče nemá přístup k kryptografickým funkcím USIM. WAF tento rozdíl překlenuje tím, že poskytuje zabezpečenou, standardizovanou metodu pro mapování přihlašovacích údajů předplatitele 3GPP na přihlašovací údaj použitelný v rámci relace WebRTC. Řeší problém silné autentizace uživatele pro provoz pocházející z webu a zajišťuje stejnou úroveň důvěry a možností účtování jako pro nativní IMS klienty. Motivací bylo přání operátorů rozšířit dosah služeb na jakékoli internetem připojené zařízení s prohlížečem, konkurovat OTT (Over-The-Top) komunikačním aplikacím a umožnit inovativní konvergované komunikační služby. Poskytuje také migrační cestu pro služby jako VoLTE, aby byly přístupné z necílových zařízení (např. notebooky, tablety), při zachování bezpečnostních a regulačních (např. zákonný odposlech) rámců jádra IMS.

## Klíčové vlastnosti

- Působí jako autentizační proxy pro klienty WebRTC k provedení GBA bootstrappingu s 3GPP BSF
- Generuje a distribuuje krátkodobé, zabezpečené autentizační tokeny (WebRTC Tokens) a přidružené klíče klientům
- Poskytuje rozhraní založená na Diameter (Mw, Mx) pro komunikaci s BSF a HSS v rámci jádrové sítě 3GPP
- Umožňuje klientům WebRTC autentizovat se vůči IMS P-CSCF pomocí varianty IMS AKA založené na tokenech
- Podporuje mapování identity předplatitele 3GPP (IMPI/IMPU) na relaci služby WebRTC
- Usnadňuje zabezpečené navázání klíčů pro šifrování médií (SRTP) mezi klientem WebRTC a sítí IMS

## Definující specifikace

- **TS 24.371** (Rel-19) — WebRTC IMS Client Access Specification
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.871** (Rel-12) — Security for WebRTC IMS Client Access

---

📖 **Anglický originál a plná specifikace:** [WAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/waf/)
