---
slug: "n3an"
url: "/mobilnisite/slovnik/n3an/"
type: "slovnik"
title: "N3AN – Non-3GPP Access Network"
date: 2025-01-01
abbr: "N3AN"
fullName: "Non-3GPP Access Network"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n3an/"
summary: "Standardizovaný referenční bod propojující síť 5G Core s přístupovou sítí non-3GPP, jako je Wi-Fi nebo pevný širokopásmový přístup. Umožňuje bezpečnou a bezproblémovou integraci alternativních přístup"
---

N3AN je standardizovaný referenční bod, který propojuje síť 5G Core s přístupovou sítí non-3GPP a umožňuje tak bezpečnou integraci technologií jako je Wi-Fi do systému 5G.

## Popis

N3AN je klíčový referenční bod definovaný v architektuře 5G System (5GS), konkrétně mezi funkcí Non-3GPP Interworking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) v jádru sítě a funkcí uživatelské roviny důvěryhodné přístupové sítě non-3GPP. Nejde o fyzické rozhraní, ale o logický bod, který standardizuje způsob připojení externích necelařských sítí k síti 5G Core (5GC). Základní protokolový zásobník pro N3AN zahrnuje [IPsec](/mobilnisite/slovnik/ipsec/) tunely zřízené nad podkladovým IP transportem. Tyto tunely přenášejí signalizaci řídicí roviny (např. pro [NAS](/mobilnisite/slovnik/nas/) zprávy mezi UE a [AMF](/mobilnisite/slovnik/amf/)) i datové pakety uživatelské roviny mezi UE a [UPF](/mobilnisite/slovnik/upf/). N3IWF funguje jako koncový bod v jádru sítě, který deenkapsuluje provoz z IPsec tunelu a směruje jej příslušným síťovým funkcím 5GC. Tato architektura umožňuje, aby síť 5GC zacházela s UE připojeným přes důvěryhodný přístup non-3GPP (jako je Wi-Fi síť spravovaná operátorem) podobně jako s UE připojeným přes 3GPP Radio Access Network (RAN), což umožňuje rozšířit klíčové funkce 5GS, jako je síťové dělení (network slicing) a konzistentní QoS, i na tyto alternativní přístupy.

Z bezpečnostního hlediska je rozhraní N3AN chráněno zřízenými IPsec Security Associations (SAs), které poskytují důvěrnost, integritu a ochranu proti opětovnému přehrání veškerého provozu procházejícího nedůvěryhodnou IP sítí mezi přístupovým bodem UE/N3AN a N3IWF. Zřizování těchto IPsec tunelů je těsně integrováno s procedurami 5G autentizace a dohody o klíčích (5G-AKA nebo EAP-AKA'). Definice N3AN zajišťuje, že jádro sítě nemusí znát konkrétní linkové technologie použité v přístupu non-3GPP, protože N3IWF poskytuje jednotné, IP-based rozhraní. Tato abstrakce je klíčová pro princip návrhu 5GS, který je nezávislý na typu přístupu.

Pokud jde o mobilitu, N3AN podporuje předávání spojení (handover) mezi přístupy 3GPP a non-3GPP. Když se například UE přesune z buňky 5G NR do důvěryhodné Wi-Fi sítě, N3AN poskytuje pokračující spojovou cestu a jádro sítě může spravovat kontinuitu relace (např. pomocí [ATSSS](/mobilnisite/slovnik/atsss/)), aniž by vrstva aplikací zaznamenala změnu podkladového přístupu. Specifikace upravující N3AN, jako jsou TS 24.502 a TS 29.525, podrobně popisují přesné toky zpráv, procedury správy tunelů a pravidla mapování QoS potřebná pro tento přeshraniční provoz, což z něj činí základní kámen pro konvergované síťové služby.

## K čemu slouží

N3AN byl vytvořen, aby řešil základní požadavek 5G na konvergovaný přístup. Před 5G byl přístup non-3GPP (především Wi-Fi) často považován za samostatnou síť druhé kategorie s omezenou integrací, využívající řešení jako S2a-based Trusted [WLAN](/mobilnisite/slovnik/wlan/) Access k EPC. To vedlo k nesourodým uživatelským zkušenostem, oddělenému ověřování a nemožnosti aplikovat konzistentní politiky a účtování na úrovni celulárních sítí. Systém 5G byl navržen od základů jako nezávislý na typu přístupu a N3AN je realizací tohoto principu pro důvěryhodné přístupy non-3GPP.

Jeho účelem je řešit problém bezproblémové kontinuity služeb a jednotného vynucování politik napříč heterogenními sítěmi. Poskytnutím standardizovaného, bezpečného rozhraní umožňuje mobilním síťovým operátorům hluboce integrovat své Wi-Fi, pevné bezdrátové nebo dokonce satelitní sítě do své 5G služební struktury. To operátorům umožňuje využít tyto alternativní sítě pro odlehčení provozu, rozšíření pokrytí a vytváření služeb svázaných s více přístupy, vše spravované z jediného 5G jádra s jednotným profilem předplatitele a politik. N3AN je tedy klíčovým prvkem umožňujícím vizi skutečně konvergovaného zážitku 'jedné sítě', který boří tradiční bariéry mezi celulárními a jinými přístupovými technologiemi.

## Klíčové vlastnosti

- Standardizovaný referenční bod pro propojení s důvěryhodným přístupem non-3GPP
- Používá IPsec tunely pro bezpečný transport přes nedůvěryhodné IP sítě
- Podporuje přenos provozu řídicí roviny (NAS) i uživatelské roviny
- Umožňuje bezproblémovou mobilitu a předávání spojení mezi přístupy 3GPP a non-3GPP
- Umožňuje rozšíření funkcí 5G Core (QoS, síťové dělení) na přístupy non-3GPP
- Integruje se s 5G autentizací (5G-AKA/EAP-AKA') pro zabezpečený přístup

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [N3AN na 3GPP Explorer](https://3gpp-explorer.com/glossary/n3an/)
