import * as React from 'react';
import Bio from '../components/bio';

const aboutPage = () => {
    return <main className='global-wrapper'>
        <title>About Me</title>
        <h1>About Me</h1>
        <p>I am a full stack Web Developer by profession and a tech enthusiast by nature.
            I am what they call 'Jack of all trades'.
        </p>
        <p>Before you get critical, let me help you with the full form:
            <pre>A jack of all trades is a master of none, but oftentimes better than a master of one.</pre>
        </p>
        <Bio />
    </main>
}

export default aboutPage;