---
slug: "vasp"
url: "/mobilnisite/slovnik/vasp/"
type: "slovnik"
title: "VASP – Value Added Service Provider"
date: 2025-01-01
abbr: "VASP"
fullName: "Value Added Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vasp/"
summary: "Entita vnější vůči mobilnímu síťovému operátorovi, která poskytuje účastníkům rozšířené telekomunikační služby. VASP vytváří a hostuje služby jako multimediální zprávy, lokalizační upozornění nebo pla"
---

VASP je entita vnější vůči mobilnímu síťovému operátorovi, která poskytuje rozšířené služby, jako jsou zprávové nebo platební systémy, prostřednictvím rozhraní s jádrem sítě operátora.

## Popis

Poskytovatel služeb s přidanou hodnotou (VASP) je základní obchodní a architektonická entita ve standardech 3GPP, která představuje organizaci nabízející služby nad rámec základních přenosových schopností (jako jsou hlasové hovory a [SMS](/mobilnisite/slovnik/sms/)) poskytovaných mobilním síťovým operátorem ([MNO](/mobilnisite/slovnik/mno/)). VASP hostuje aplikační logiku, obsah a prostředí pro provádění služeb. Připojuje se k síti operátora prostřednictvím definovaných referenčních bodů, jako jsou rozhraní Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) nebo Parlay, nebo prostřednictvím služebně specifických bran, jako je Multimedia Messaging Service Centre (MMSC) nebo aplikační server IP Multimedia Subsystem (IMS).

Architektonicky se VASP nachází v důvěryhodné doméně a často vyžaduje formální obchodní dohodu s MNO. Připojení je zprostředkováno bránou nebo serverem schopností služeb ([SCS](/mobilnisite/slovnik/scs/)), který poskytuje standardizované, bezpečné [API](/mobilnisite/slovnik/api/). Tato abstraktní vrstva chrání jádro sítě před přímým vystavením a zároveň poskytuje VASP řízený přístup k síťovým schopnostem, jako je odesílání SMS, dotazování na polohu účastníka (s jeho souhlasem) nebo zahájení hovoru. Platforma VASP je zodpovědná za autentizaci uživatele, logiku služby, správu obsahu a často se rozhraní s vlastními fakturačními systémy, ačkoli fakturační data jsou obvykle korelována se systémy MNO pro integrované účtování.

Jak to funguje, zahrnuje spouštěč služby. Například účastník může odeslat SMS na krátké číslo vlastněné VASP pro povětrnostní upozornění. SM-SC operátora MNO tuto zprávu směruje na platformu VASP. VASP žádost zpracuje, načte příslušná povětrnostní data a vytvoří odpověď ve formě SMS. Poté použije síťové rozhraní k odeslání této odpovědi zpět do SM-SC pro doručení účastníkovi. Síť MNO generuje záznamy o účtování za výměnu zpráv a příjmy mohou být sdíleny podle obchodní dohody. Role VASP tedy spočívá v obohacení uživatelského zážitku využitím síťových prostředků k vytváření prodejných, inovativních služeb, které si MNO nemusí vyvíjet vlastními silami.

## K čemu slouží

Koncept VASP byl formalizován za účelem podpory otevřeného, konkurenčního trhu pro mobilní služby. Síťoví operátoři vlastní infrastrukturu, ale mohou postrádat pružnost nebo specializované know-how pro vývoj široké škály aplikací. Účelem definice role VASP je oddělit tvorbu služeb od provozu sítě a umožnit tak specializovaným společnostem inovovat. Tím vzniká živý ekosystém, kde operátoři poskytují konektivitu a umožňující prvky, zatímco VASP se zaměřují na vytváření atraktivních služeb pro koncové uživatele, což zvyšuje zapojení účastníků a generuje sdílené příjmy.

Historicky, před existencí jasných rámců pro VASP, byly pokročilé služby buď zcela budovány operátorem (což omezovalo rozmanitost), nebo prostřednictvím proprietárních, neškálovatelných integrací. Standardizace role VASP v rámci 3GPP, zejména prostřednictvím iniciativ jako Open Service Architecture ([OSA](/mobilnisite/slovnik/osa/)), řešila potřebu bezpečného a standardizovaného zpřístupnění sítě. Vyřešila kritické problémy: poskytla jasný komerční a technický model pro přístup třetích stran, definovala bezpečnostní hranice pro ochranu sítě a stanovila účtovací mechanismy, které zajistily, že všechny strany mohou být kompenzovány. To umožnilo explozi služeb, jako jsou stahování vyzváněcích melodií, multimediální zprávy, mobilní hry a podniková řešení v éře 2G/3G, a položilo základy pro moderní zpřístupňování založené na [API](/mobilnisite/slovnik/api/) v sítích 4G a 5G.

## Klíčové vlastnosti

- Definován jako externí entita poskytující služby nad rámec základních přenosových schopností
- Propojuje se s jádrem mobilní sítě prostřednictvím standardizovaných rozhraní (např. OSA/Parlay, IMS Service Control)
- Hostuje aplikační logiku, obsah a prostředí pro provádění služeb
- Funguje na základě obchodní dohody s mobilním síťovým operátorem (MNO)
- Může využívat síťové umožňující prvky, jako jsou zprávové služby, lokalizace a řízení hovorů
- Podílí se na modelech sdílení příjmů založených na využívání služeb

## Související pojmy

- [OSA – Open Services Architecture](/mobilnisite/slovnik/osa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.140** (Rel-19) — MMS Stage 1 Requirements
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [VASP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vasp/)
